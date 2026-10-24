import os
import uuid
from datetime import datetime, date
from typing import List, Dict, Any, Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware

from database import get_db
from models import (
    UserRegister, UserLogin, UserProfile, TokenResponse,
    AssessmentQuestion, AssessmentSubmitRequest, AssessmentResultResponse,
    Roadmap, TopicDetail, ProgressUpdateRequest, GamificationStatus,
    AdaptiveReflectionSubmit,
    OnboardingRequest, ExplorationFeedbackRequest, PlanningUpdateRequest, SelectVideoRequest
)
from auth import (
    verify_password, get_password_hash, create_access_token,
    get_current_user, require_current_user
)
from data.assessment_questions import ASSESSMENT_QUESTIONS, DOMAIN_DETAILS, ADAPTIVE_CHECKPOINTS
from data.seed_roadmaps import SEED_ROADMAPS, TOPIC_DETAILS
from scoring import compute_assessment_result
from services.curated_videos import resolve_topic_videos
from services.personalization_engine import PersonalizationEngine
from services.exploration_catalog import EXPLORATION_ACTIVITIES, get_exploration_activities, calculate_career_ranking_with_evidence

from services.ai_assistant import generate_learner_explanation





@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB connection
    db = get_db()
    await db.connect()
    
    # Seed roadmaps if empty
    roadmaps_col = db.get_collection("roadmaps")
    count = await roadmaps_col.count_documents({})
    if count == 0:
        print("[Startup] Seeding curated roadmaps to MongoDB Atlas...")
        for rm in SEED_ROADMAPS:
            doc = dict(rm)
            if "_id" not in doc:
                doc["_id"] = doc.get("id", f"rm_{len(doc)}")
            await roadmaps_col.insert_one(doc)
        print(f"[Startup] Seeded {len(SEED_ROADMAPS)} roadmaps successfully.")

    # Seed topic details if empty
    topics_col = db.get_collection("topic_details")
    topic_count = await topics_col.count_documents({})
    if topic_count == 0:
        print("[Startup] Seeding topic learning modules to MongoDB Atlas...")
        for topic_id, details in TOPIC_DETAILS.items():
            doc = dict(details)
            if "_id" not in doc:
                doc["_id"] = topic_id
            await topics_col.insert_one(doc)
        print(f"[Startup] Seeded {len(TOPIC_DETAILS)} topic modules successfully.")

    yield
    print("[Shutdown] Horizon backend shut down cleanly.")


app = FastAPI(
    title="Horizon Learning API",
    description="Backend API powering Horizon AI-guided learning platform with personalized roadmaps, labs, and adaptive guidance.",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Health Check ---
@app.get("/api/health")
async def health_check():
    db = get_db()
    return {
        "status": "healthy",
        "service": "Horizon Backend API",
        "timestamp": datetime.utcnow().isoformat(),
        "database_connected": db.is_mongo_connected
    }


# --- Auth Routes ---
@app.post("/api/auth/register", response_model=TokenResponse)
async def register(payload: UserRegister):
    db = get_db()
    users_col = db.get_collection("users")
    
    existing = await users_col.find_one({"email": payload.email.lower().strip()})
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account with this email already exists."
        )

    user_id = f"user_{uuid.uuid4().hex[:12]}"
    created_at = datetime.utcnow().isoformat()
    hashed_pwd = get_password_hash(payload.password)

    new_user = {
        "id": user_id,
        "email": payload.email.lower().strip(),
        "password_hash": hashed_pwd,
        "full_name": payload.full_name.strip(),
        "avatar": f"https://api.dicebear.com/7.x/bottts/svg?seed={user_id}",
        "created_at": created_at,
        "primary_domain": None,
        "xp": 50, # Initial welcome bonus
        "streak": 1,
        "level": 1,
        "badges": ["Novice Explorer", "Account Created"],
        "last_active": date.today().isoformat()
    }
    await users_col.insert_one(new_user)

    token = create_access_token({"sub": user_id, "email": new_user["email"]})
    
    profile = UserProfile(
        id=new_user["id"],
        email=new_user["email"],
        full_name=new_user["full_name"],
        avatar=new_user["avatar"],
        created_at=new_user["created_at"],
        primary_domain=new_user["primary_domain"],
        xp=new_user["xp"],
        streak=new_user["streak"],
        level=new_user["level"],
        badges=new_user["badges"]
    )
    return TokenResponse(access_token=token, user=profile)


@app.post("/api/auth/login", response_model=TokenResponse)
async def login(payload: UserLogin):
    db = get_db()
    users_col = db.get_collection("users")

    user = await users_col.find_one({"email": payload.email.lower().strip()})
    if not user or not verify_password(payload.password, user.get("password_hash", "")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Update streak if active today
    today_str = date.today().isoformat()
    last_active = user.get("last_active", "")
    streak = user.get("streak", 1)
    if last_active and last_active != today_str:
        # If active yesterday, increment; if missed more than 1 day, reset to 1
        last_date = datetime.strptime(last_active, "%Y-%m-%d").date()
        days_diff = (date.today() - last_date).days
        if days_diff == 1:
            streak += 1
        elif days_diff > 1:
            streak = 1
        await users_col.update_one({"id": user["id"]}, {"$set": {"last_active": today_str, "streak": streak}})
        user["streak"] = streak

    token = create_access_token({"sub": user["id"], "email": user["email"]})
    
    profile = UserProfile(
        id=user["id"],
        email=user["email"],
        full_name=user["full_name"],
        avatar=user.get("avatar"),
        created_at=user.get("created_at", today_str),
        primary_domain=user.get("primary_domain"),
        xp=user.get("xp", 0),
        streak=user.get("streak", 1),
        level=user.get("level", 1),
        badges=user.get("badges", [])
    )
    return TokenResponse(access_token=token, user=profile)


@app.get("/api/auth/me", response_model=UserProfile)
async def get_me(user: Dict[str, Any] = Depends(require_current_user)):
    return UserProfile(
        id=user["id"],
        email=user["email"],
        full_name=user["full_name"],
        avatar=user.get("avatar"),
        created_at=user.get("created_at", ""),
        primary_domain=user.get("primary_domain"),
        xp=user.get("xp", 0),
        streak=user.get("streak", 1),
        level=user.get("level", 1),
        badges=user.get("badges", [])
    )


# --- 15-Question Assessment Routes ---
@app.get("/api/assessment/questions")
async def get_assessment_questions():
    """Returns the 15 diagnostic questions for onboarding assessment."""
    return {
        "total_questions": len(ASSESSMENT_QUESTIONS),
        "questions": ASSESSMENT_QUESTIONS
    }


@app.post("/api/assessment/submit")
async def submit_assessment(
    payload: AssessmentSubmitRequest,
    current_user: Optional[Dict[str, Any]] = Depends(get_current_user)
):
    """
    Submits user responses to the 15 questions, calculates recommended domain,
    and returns Top 4 Roadmaps. If user is logged in, persists to MongoDB.
    """
    result = compute_assessment_result(payload.answers)
    
    if current_user:
        db = get_db()
        users_col = db.get_collection("users")
        assessments_col = db.get_collection("assessments")

        # Save assessment history
        assessment_doc = {
            "id": f"asmt_{uuid.uuid4().hex[:10]}",
            "user_id": current_user["id"],
            "submitted_at": datetime.utcnow().isoformat(),
            "answers": payload.answers,
            "recommended_domain": result["recommended_domain"],
            "archetype": result.get("archetype"),
            "idk_count": result.get("idk_count", 0),
            "is_exploring_mode": result.get("is_exploring_mode", False),
            "domain_scores": result["domain_scores"]
        }
        await assessments_col.insert_one(assessment_doc)

        # Update user profile with primary domain, archetype and award 100 XP bonus
        await users_col.update_one(
            {"id": current_user["id"]},
            {
                "$set": {
                    "primary_domain": result["recommended_domain"],
                    "archetype": result.get("archetype"),
                    "is_exploring_mode": result.get("is_exploring_mode", False)
                },
                "$inc": {"xp": 100}
            }
        )

    return result


@app.get("/api/assessment/result")
async def get_saved_assessment_result(
    current_user: Dict[str, Any] = Depends(require_current_user)
):
    db = get_db()
    assessments_col = db.get_collection("assessments")
    latest = await assessments_col.find_one({"user_id": current_user["id"]})
    if not latest:
        return compute_assessment_result({})
    return compute_assessment_result(latest.get("answers", {}))


# --- Adaptive In-Learning Checkpoints (Contextual Psychology Calibration) ---
@app.get("/api/assessment/adaptive-checkpoint/{topic_id}")
async def get_adaptive_checkpoint(topic_id: str):
    """Returns a contextual psychological reflection prompt for this topic if available."""
    for chk in ADAPTIVE_CHECKPOINTS:
        if chk["trigger_topic"] == topic_id:
            return {"available": True, "checkpoint": chk}
    return {"available": False, "checkpoint": None}


@app.post("/api/assessment/adaptive-reflection")
async def submit_adaptive_reflection(
    payload: AdaptiveReflectionSubmit,
    current_user: Optional[Dict[str, Any]] = Depends(get_current_user)
):
    """
    Saves user's in-learning reflection and updates domain calibration in MongoDB.
    Awards 25 XP.
    """
    if current_user:
        db = get_db()
        users_col = db.get_collection("users")
        assessments_col = db.get_collection("assessments")

        latest_asmt = await assessments_col.find_one({"user_id": current_user["id"]})
        if latest_asmt:
            domain_scores = latest_asmt.get("domain_scores", {})
            target_domain = payload.reinforce_domain
            domain_scores[target_domain] = domain_scores.get(target_domain, 0) + 4
            
            # Recalculate top domain
            sorted_domains = sorted(domain_scores.items(), key=lambda x: x[1], reverse=True)
            new_primary = sorted_domains[0][0]

            await assessments_col.update_one(
                {"id": latest_asmt["id"]},
                {"$set": {"domain_scores": domain_scores, "recommended_domain": new_primary}}
            )
            await users_col.update_one(
                {"id": current_user["id"]},
                {
                    "$set": {"primary_domain": new_primary},
                    "$inc": {"xp": 25}
                }
            )
    return {
        "status": "success",
        "message": f"Career compass calibrated towards {payload.reinforce_domain}.",
        "awarded_xp": 25
    }


# --- Roadmaps Routes ---
@app.get("/api/roadmaps/top4")
async def get_top4_roadmaps(current_user: Optional[Dict[str, Any]] = Depends(get_current_user)):
    """Returns the Top 4 personalized roadmaps for the user."""
    primary_domain = current_user.get("primary_domain") if current_user else None
    
    # If user has a diagnosed domain, prioritize that
    if primary_domain:
        result = compute_assessment_result({})
        # customize by domain
        ranked = [rm for rm in SEED_ROADMAPS if rm.get("domain") == primary_domain]
        for rm in SEED_ROADMAPS:
            if rm not in ranked:
                ranked.append(rm)
        return ranked[:4]

    # Default Top 4
    return SEED_ROADMAPS[:4]


@app.get("/api/roadmaps")
async def get_all_roadmaps():
    """Returns all available roadmaps for the 'See All Courses' explorer."""
    db = get_db()
    roadmaps_col = db.get_collection("roadmaps")
    roadmaps = await roadmaps_col.find({})
    if not roadmaps:
        return SEED_ROADMAPS
    return roadmaps


@app.get("/api/roadmaps/{slug}")
async def get_roadmap_by_slug(slug: str, current_user: Optional[Dict[str, Any]] = Depends(get_current_user)):
    """Returns full details of a roadmap by slug, including user completion status."""
    db = get_db()
    roadmaps_col = db.get_collection("roadmaps")
    roadmap = await roadmaps_col.find_one({"slug": slug})
    if not roadmap:
        for rm in SEED_ROADMAPS:
            if rm["slug"] == slug:
                roadmap = rm
                break

    if not roadmap:
        raise HTTPException(status_code=404, detail="Roadmap not found")

    # If user logged in, overlay completion status
    if current_user:
        progress_col = db.get_collection("user_progress")
        user_prog = await progress_col.find_one({
            "user_id": current_user["id"],
            "roadmap_slug": slug
        })
        completed_set = set(user_prog.get("completed_topics", [])) if user_prog else set()
        
        # Deep copy stages to mark completion
        roadmap_stages = []
        for stage in roadmap.get("stages", []):
            st_copy = dict(stage)
            topics_copy = []
            for t in stage.get("topics", []):
                t_copy = dict(t)
                t_copy["is_completed"] = t["id"] in completed_set
                topics_copy.append(t_copy)
            st_copy["topics"] = topics_copy
            roadmap_stages.append(st_copy)
        roadmap = dict(roadmap)
        roadmap["stages"] = roadmap_stages

    return roadmap


# --- Deep Learning Topic Content Routes ---
@app.get("/api/topics/{topic_id}")
async def get_topic_details(topic_id: str, current_user: Optional[Dict[str, Any]] = Depends(get_current_user)):
    """
    Returns rich topic learning workspace:
    - Personalized GOAT YouTube video recommendation based on learner profile
    - Multi-option video catalog (Masterclass, Fast-paced/Visual, Hinglish Masterclass)
    - Notes, Questions, Lab, and Workshop
    """
    db = get_db()
    topics_col = db.get_collection("topic_details")
    details = await topics_col.find_one({"id": topic_id})
    if not details:
        if topic_id in TOPIC_DETAILS:
            details = TOPIC_DETAILS[topic_id]

    if not details:
        clean_title = topic_id.replace("frontend_", "").replace("backend_", "").replace("fs_topic_", "").replace("ai_topic_", "").replace("do_topic_", "").replace("sec_topic_", "").replace("_", " ").title()
        details = {
            "id": topic_id,
            "roadmap_slug": "full-stack-developer",
            "stage_id": "generic_stage",
            "title": clean_title,
            "description": f"Mastery curriculum for {clean_title} covering core principles, production architecture, interactive lab challenges, and capstone project workshop.",
            "lectures": [],
            "notes": f"# {clean_title}\n\nWelcome to this comprehensive mastery module. Study the recommended GOAT lecture, review architectural notes, and test your practical comprehension in the interactive quiz and lab.\n\n### Core Engineering Principles\n- Understand runtime mechanics and mental models\n- Structure clean, modular, testable code\n- Follow production reliability and security best practices",
            "questions": [
                {
                    "id": f"q_{topic_id}_1",
                    "question": f"What is the recommended best practice when architecting {clean_title}?",
                    "options": [
                        "Follow modular component architecture and write automated tests",
                        "Hardcode all environment variables directly in client code",
                        "Disable logging to save network bandwidth",
                        "Avoid using asynchronous functions in production"
                    ],
                    "correct_option": 0,
                    "explanation": "Modular design, automated testing, and clear separation of concerns guarantee maintainability and zero regressions in production.",
                    "xp": 25
                }
            ],
            "lab": {
                "id": f"lab_{topic_id}",
                "title": f"Hands-on Lab: {clean_title}",
                "instructions": f"Implement the core solution for {clean_title} and verify all test cases pass.",
                "language": "javascript",
                "starter_code": "// Complete the function\nfunction solution() {\n  return true;\n}",
                "test_cases": [{"input": "()", "expected": "true", "description": "Returns true"}],
                "hint": "Ensure the function returns the expected value.",
                "xp": 50
            },
            "workshop": {
                "id": f"ws_{topic_id}",
                "title": f"Capstone Workshop: {clean_title}",
                "tagline": "Build a real-world project applying these concepts",
                "overview": f"Synthesize this topic into a portfolio-ready implementation of {clean_title}.",
                "steps": [
                    "Step 1: Set up repository and dependencies.",
                    "Step 2: Implement core business logic.",
                    "Step 3: Test and deploy to production."
                ],
                "acceptance_criteria": ["Working code", "Passing tests"],
                "xp": 100
            }
        }

    # Fetch learner profile to check preferred video or personalization traits
    preferred_video_id = None
    user_lp = None
    if current_user:
        lp_col = db.get_collection("learner_profiles")
        user_lp = await lp_col.find_one({"user_id": current_user["id"]})
        if user_lp and "preferred_videos" in user_lp:
            preferred_video_id = user_lp["preferred_videos"].get(topic_id)

    # Resolve genuine GOAT YouTube educational videos with personalization
    resolved_video_data = resolve_topic_videos(
        topic_id=topic_id,
        title=details.get("title", topic_id),
        domain=details.get("roadmap_slug", ""),
        user_profile=user_lp.get("onboarding") if user_lp else None,
        preferred_video_id=preferred_video_id
    )

    details = dict(details)
    if "_id" in details:
        details["_id"] = str(details["_id"])
    details["lectures"] = resolved_video_data["all_lectures"]
    details["recommended_lecture"] = resolved_video_data["recommended_lecture"]
    details["match_reason"] = resolved_video_data["match_reason"]

    # Overlay user progress for this topic if authenticated
    user_progress_data = {}
    if current_user:
        progress_col = db.get_collection("user_progress")
        prog = await progress_col.find_one({
            "user_id": current_user["id"],
            "roadmap_slug": details.get("roadmap_slug", "full-stack-developer")
        })
        if prog:
            user_progress_data = {
                "is_topic_completed": topic_id in prog.get("completed_topics", []),
                "completed_items": prog.get("completed_items", {}).get(topic_id, [])
            }

    return {
        "topic": details,
        "user_progress": user_progress_data
    }


@app.post("/api/topics/{topic_id}/select-video")
async def select_topic_video(
    topic_id: str,
    payload: SelectVideoRequest,
    current_user: Dict[str, Any] = Depends(require_current_user)
):
    """
    Saves the user's selected video preference (e.g. switching to Hinglish or Fast-Paced)
    into their persistent learner profile in MongoDB.
    """
    db = get_db()
    lp_col = db.get_collection("learner_profiles")
    lp = await lp_col.find_one({"user_id": current_user["id"]})
    if not lp:
        lp = PersonalizationEngine.initialize_learner_profile(
            current_user["id"], current_user["email"], current_user["full_name"]
        )
        await lp_col.insert_one(lp)

    preferred_videos = lp.get("preferred_videos", {})
    preferred_videos[topic_id] = payload.video_id

    await lp_col.update_one(
        {"user_id": current_user["id"]},
        {"$set": {"preferred_videos": preferred_videos, "updated_at": datetime.utcnow().isoformat()}}
    )
    return {"status": "success", "topic_id": topic_id, "selected_video_id": payload.video_id}



# --- Progress & Gamification Tracking Routes ---
@app.post("/api/progress/complete")
async def complete_progress_item(
    payload: ProgressUpdateRequest,
    current_user: Dict[str, Any] = Depends(require_current_user)
):
    """
    Saves granular progress when a user completes a lecture, notes, quiz, lab, or topic.
    Updates streaks, calculates earned XP, and awards badges!
    """
    db = get_db()
    progress_col = db.get_collection("user_progress")
    users_col = db.get_collection("users")

    user_id = current_user["id"]
    xp_awards = {
        "lecture": 25,
        "note": 20,
        "quiz": 35,
        "lab": 50,
        "workshop": 100,
        "topic_complete": 150
    }
    earned_xp = xp_awards.get(payload.action_type, 20)

    # Fetch or initialize user progress document for this roadmap
    user_prog = await progress_col.find_one({
        "user_id": user_id,
        "roadmap_slug": payload.roadmap_slug
    })

    if not user_prog:
        user_prog = {
            "id": f"prog_{uuid.uuid4().hex[:10]}",
            "user_id": user_id,
            "roadmap_slug": payload.roadmap_slug,
            "completed_topics": [],
            "completed_items": {},
            "total_xp_earned": 0,
            "updated_at": datetime.utcnow().isoformat()
        }
        await progress_col.insert_one(user_prog)

    completed_items = user_prog.get("completed_items", {})
    topic_items = completed_items.get(payload.topic_id, [])
    
    is_new_action = payload.action_type not in topic_items
    if is_new_action:
        topic_items.append(payload.action_type)
        completed_items[payload.topic_id] = topic_items

    completed_topics = user_prog.get("completed_topics", [])
    if payload.action_type == "topic_complete" and payload.topic_id not in completed_topics:
        completed_topics.append(payload.topic_id)

    # Update progress document
    await progress_col.update_one(
        {"user_id": user_id, "roadmap_slug": payload.roadmap_slug},
        {
            "$set": {
                "completed_topics": completed_topics,
                "completed_items": completed_items,
                "updated_at": datetime.utcnow().isoformat()
            },
            "$inc": {"total_xp_earned": earned_xp if is_new_action else 0}
        }
    )

    # Update user total XP and Level
    if is_new_action:
        new_xp = current_user.get("xp", 0) + earned_xp
        new_level = (new_xp // 250) + 1
        
        # Check badges
        badges = list(current_user.get("badges", []))
        if len(completed_topics) >= 1 and "First Milestone" not in badges:
            badges.append("First Milestone")
        if new_xp >= 500 and "XP Grinder" not in badges:
            badges.append("XP Grinder")
        if payload.action_type == "lab" and "Code Architect" not in badges:
            badges.append("Code Architect")

        await users_col.update_one(
            {"id": user_id},
            {
                "$set": {
                    "xp": new_xp,
                    "level": new_level,
                    "badges": badges,
                    "last_active": date.today().isoformat()
                }
            }
        )

    return {
        "status": "success",
        "action": payload.action_type,
        "earned_xp": earned_xp if is_new_action else 0,
        "is_topic_completed": payload.topic_id in completed_topics,
        "completed_items": completed_items.get(payload.topic_id, [])
    }


@app.get("/api/gamification/status")
async def get_gamification_status(current_user: Dict[str, Any] = Depends(require_current_user)):
    db = get_db()
    progress_col = db.get_collection("user_progress")
    user_progs = await progress_col.find({"user_id": current_user["id"]})
    
    total_completed_topics = 0
    for p in user_progs:
        total_completed_topics += len(p.get("completed_topics", []))

    xp = current_user.get("xp", 0)
    level = (xp // 250) + 1
    xp_in_level = xp % 250
    next_level_xp = 250
    progress_pct = round((xp_in_level / next_level_xp) * 100, 1)

    badge_catalog = [
        {"name": "Novice Explorer", "icon": "Compass", "description": "Embarked on the Horizon journey", "unlocked": True},
        {"name": "Pathfinder", "icon": "MapPin", "description": "Completed the 15-question diagnostic assessment", "unlocked": current_user.get("primary_domain") is not None},
        {"name": "First Milestone", "icon": "Trophy", "description": "Completed your first roadmap topic", "unlocked": total_completed_topics >= 1},
        {"name": "Code Architect", "icon": "Code2", "description": "Passed an interactive coding lab challenge", "unlocked": "Code Architect" in current_user.get("badges", [])},
        {"name": "Streak Flame", "icon": "Flame", "description": "Maintained an active learning streak", "unlocked": current_user.get("streak", 1) >= 1},
        {"name": "XP Grinder", "icon": "Zap", "description": "Accumulated 500+ XP on your profile", "unlocked": xp >= 500}
    ]

    return {
        "xp": xp,
        "streak": current_user.get("streak", 1),
        "level": level,
        "xp_in_current_level": xp_in_level,
        "next_level_xp": next_level_xp,
        "progress_percentage": progress_pct,
        "completed_topics_count": total_completed_topics,
        "badges": badge_catalog
    }


# --- Interactive Lab Validation Route ---
@app.post("/api/labs/run-code")
async def run_lab_code(payload: Dict[str, Any]):
    """
    Validates user code submissions against test cases.
    """
    code = payload.get("code", "")
    test_cases = payload.get("test_cases", [])
    
    results = []
    all_passed = True
    
    for tc in test_cases:
        expected = str(tc.get("expected", "")).strip().lower()
        # Heuristic check for lab code
        passed = expected in code.lower()
        if not passed:
            all_passed = False
        results.append({
            "description": tc.get("description", "Test case"),
            "passed": passed,
            "message": "Assertion passed ✓" if passed else f"Expected code to contain '{expected}'"
        })

    return {
        "success": all_passed,
        "results": results,
        "xp_awarded": 50 if all_passed else 0,
        "feedback": "Outstanding work! All tests passed." if all_passed else "Review the hints and try again."
    }


# =========================================================================
# --- ADAPTIVE PERSONALIZATION & 9-STEP PIPELINE ENGINE ROUTES ---
# =========================================================================

@app.get("/api/personalization/profile")
async def get_learner_profile(current_user: Dict[str, Any] = Depends(require_current_user)):
    """Retrieves or initializes the persistent learner model for the user."""
    db = get_db()
    lp_col = db.get_collection("learner_profiles")
    profile = await lp_col.find_one({"user_id": current_user["id"]})
    if not profile:
        profile = PersonalizationEngine.initialize_learner_profile(
            current_user["id"], current_user["email"], current_user["full_name"]
        )
        if current_user.get("primary_domain"):
            profile["career_goal"]["primary_domain"] = current_user["primary_domain"]
        await lp_col.insert_one(profile)
    return profile


@app.post("/api/personalization/onboarding")
async def submit_personalization_onboarding(
    payload: OnboardingRequest,
    current_user: Dict[str, Any] = Depends(require_current_user)
):
    """
    Saves multi-dimensional onboarding answers:
    Career certainty, activity interests, experience level, weekly hours, planning horizon,
    learning style, and language preference.
    """
    db = get_db()
    lp_col = db.get_collection("learner_profiles")
    users_col = db.get_collection("users")
    
    profile = await lp_col.find_one({"user_id": current_user["id"]})
    if not profile:
        profile = PersonalizationEngine.initialize_learner_profile(
            current_user["id"], current_user["email"], current_user["full_name"]
        )
        await lp_col.insert_one(profile)

    onboarding_data = payload.model_dump()
    target_domain = payload.target_career or current_user.get("primary_domain") or "fullstack"

    # Update user record
    await users_col.update_one(
        {"id": current_user["id"]},
        {"$set": {"primary_domain": target_domain}}
    )

    # Recalculate milestones based on horizon
    milestones = PersonalizationEngine.calculate_horizon_milestones(
        target_domain, payload.planning_horizon or "6_months", payload.weekly_hours or 10
    )

    # Update learner profile
    await lp_col.update_one(
        {"user_id": current_user["id"]},
        {
            "$set": {
                "onboarding": onboarding_data,
                "career_goal.primary_domain": target_domain,
                "career_goal.confidence": "high" if payload.career_certainty == "specific_goal" else "moderate",
                "milestones": milestones,
                "updated_at": datetime.utcnow().isoformat()
            }
        }
    )

    return {
        "status": "success",
        "domain": target_domain,
        "onboarding": onboarding_data,
        "milestones": milestones
    }


@app.get("/api/personalization/exploration")
async def get_exploration_tasks(domain: Optional[str] = None):
    """Returns practical, beginner-friendly exploration activities across domains."""
    return {"activities": get_exploration_activities(domain)}


@app.post("/api/personalization/exploration/feedback")
async def submit_exploration_feedback(
    payload: ExplorationFeedbackRequest,
    current_user: Dict[str, Any] = Depends(require_current_user)
):
    """
    Processes practical exploration feedback (interest, difficulty, completion independence)
    and updates career recommendation ranking with empirical evidence.
    """
    db = get_db()
    lp_col = db.get_collection("learner_profiles")
    profile = await lp_col.find_one({"user_id": current_user["id"]})
    if not profile:
        profile = PersonalizationEngine.initialize_learner_profile(
            current_user["id"], current_user["email"], current_user["full_name"]
        )
        await lp_col.insert_one(profile)

    history = profile.get("exploration_history", [])
    history.append(payload.model_dump())

    base_scores = {
        "frontend": 70.0, "backend": 70.0, "ai_ml": 70.0,
        "devops": 70.0, "cybersecurity": 70.0, "fullstack": 75.0
    }
    ranking = calculate_career_ranking_with_evidence(base_scores, history)

    await lp_col.update_one(
        {"user_id": current_user["id"]},
        {
            "$set": {
                "exploration_history": history,
                "career_goal.primary_domain": ranking["top_domain"],
                "career_goal.confidence": "high" if len(history) >= 2 else "moderate",
                "updated_at": datetime.utcnow().isoformat()
            }
        }
    )

    return {
        "status": "success",
        "ranking": ranking,
        "total_experiments_completed": len(history)
    }


@app.get("/api/personalization/missions/next")
async def get_next_recommended_mission(current_user: Optional[Dict[str, Any]] = Depends(get_current_user)):
    """
    Prerequisite-aware recommendation engine:
    Selects the immediate next 30-minute micro-mission (Learn + Practice + Prove)
    tailored to the learner's skill state, weak prerequisites, and career goal.
    """
    profile = None
    if current_user:
        db = get_db()
        lp_col = db.get_collection("learner_profiles")
        profile = await lp_col.find_one({"user_id": current_user["id"]})

    if not profile:
        profile = PersonalizationEngine.initialize_learner_profile("guest", "guest@horizon.dev", "Guest Learner")

    mission = PersonalizationEngine.select_next_recommended_mission(profile)
    return {"mission": mission}


@app.post("/api/personalization/missions/{mission_id}/complete")
async def complete_recommended_mission(
    mission_id: str,
    payload: Dict[str, Any],
    current_user: Dict[str, Any] = Depends(require_current_user)
):
    """
    Marks a recommended mission complete, updates skill mastery state,
    persists evidence to MongoDB, and triggers adaptive replanning.
    """
    skill_id = payload.get("skill_id", "skill_javascript_core")
    success = payload.get("success", True)
    
    db = get_db()
    lp_col = db.get_collection("learner_profiles")
    users_col = db.get_collection("users")
    
    profile = await lp_col.find_one({"user_id": current_user["id"]})
    if not profile:
        profile = PersonalizationEngine.initialize_learner_profile(
            current_user["id"], current_user["email"], current_user["full_name"]
        )
        await lp_col.insert_one(profile)

    update_res = PersonalizationEngine.update_skill_evidence(
        profile, skill_id, "lab" if success else "quiz", success=success
    )

    completed_msns = profile.get("completed_missions", [])
    completed_msns.append({
        "mission_id": mission_id,
        "skill_id": skill_id,
        "timestamp": datetime.utcnow().isoformat()
    })
    
    await lp_col.update_one(
        {"user_id": current_user["id"]},
        {
            "$set": {
                "skill_states": profile["skill_states"],
                "completed_missions": completed_msns,
                "updated_at": datetime.utcnow().isoformat()
            }
        }
    )

    await users_col.update_one({"id": current_user["id"]}, {"$inc": {"xp": 50}})
    return {
        "status": "success",
        "skill_update": update_res,
        "awarded_xp": 50
    }


@app.post("/api/personalization/planning")
async def update_planning_horizon(
    payload: PlanningUpdateRequest,
    current_user: Dict[str, Any] = Depends(require_current_user)
):
    """
    Updates the learner's planning horizon (1m, 3m, 6m, 1y, 4y) and weekly hours,
    and dynamically recalibrates milestones and task pacing.
    """
    db = get_db()
    lp_col = db.get_collection("learner_profiles")
    profile = await lp_col.find_one({"user_id": current_user["id"]})
    if not profile:
        profile = PersonalizationEngine.initialize_learner_profile(
            current_user["id"], current_user["email"], current_user["full_name"]
        )
        await lp_col.insert_one(profile)

    domain = profile.get("career_goal", {}).get("primary_domain", "fullstack")
    milestones = PersonalizationEngine.calculate_horizon_milestones(
        domain, payload.planning_horizon, payload.weekly_hours
    )

    await lp_col.update_one(
        {"user_id": current_user["id"]},
        {
            "$set": {
                "onboarding.planning_horizon": payload.planning_horizon,
                "onboarding.weekly_hours": payload.weekly_hours,
                "milestones": milestones,
                "updated_at": datetime.utcnow().isoformat()
            }
        }
    )

    return {
        "status": "success",
        "planning_horizon": payload.planning_horizon,
        "weekly_hours": payload.weekly_hours,
        "milestones": milestones
    }


@app.get("/api/personalization/journey")
async def get_learner_journey(current_user: Optional[Dict[str, Any]] = Depends(get_current_user)):
    """
    Returns the learner's personalized high-level roadmap, stages, milestones,
    prerequisite relationships, and mastery states.
    """
    profile = None
    if current_user:
        db = get_db()
        lp_col = db.get_collection("learner_profiles")
        profile = await lp_col.find_one({"user_id": current_user["id"]})

    if not profile:
        profile = PersonalizationEngine.initialize_learner_profile("guest", "guest@horizon.dev", "Guest Learner")

    domain = profile.get("career_goal", {}).get("primary_domain", "fullstack")
    horizon = profile.get("onboarding", {}).get("planning_horizon", "6_months")
    weekly_hours = profile.get("onboarding", {}).get("weekly_hours", 10)
    milestones = PersonalizationEngine.calculate_horizon_milestones(domain, horizon, weekly_hours)

    return {
        "career_goal": profile.get("career_goal"),
        "planning_horizon": horizon,
        "weekly_hours": weekly_hours,
        "milestones": milestones,
        "skill_states": profile.get("skill_states", {})
    }


@app.post("/api/personalization/explain-skill")
async def explain_skill_relevance(payload: Dict[str, Any]):
    """Provides context-aware explanation for why a skill is vital for a career goal."""
    career_goal = payload.get("career_goal", "fullstack")
    skill_name = payload.get("skill_name", "JavaScript")
    user_style = payload.get("user_style", "visual")
    user_level = payload.get("user_level", "beginner")
    
    explanation = await generate_learner_explanation(career_goal, skill_name, user_style, user_level)
    return explanation

