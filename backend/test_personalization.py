"""
Comprehensive Test Suite for Horizon's Adaptive Personalization Engine,
Curated GOAT YouTube Videos, Prerequisite Graph, and Missions.
"""

import asyncio
import httpx
from main import app
from services.personalization_engine import PersonalizationEngine, CANONICAL_SKILL_GRAPH, validate_canonical_graph
from services.curated_videos import resolve_topic_videos, CURATED_GOAT_CATALOG
from services.exploration_catalog import get_exploration_activities, calculate_career_ranking_with_evidence


async def run_personalization_tests():
    print("=== STARTING HORIZON ADAPTIVE PERSONALIZATION ENGINE TESTS ===")

    # 1. Test Canonical Skill Graph Integrity
    valid, errors = validate_canonical_graph()
    assert valid is True, f"Graph validation errors: {errors}"
    print(f"[PASS] Canonical Skill Graph validated: {len(CANONICAL_SKILL_GRAPH)} skills with zero cycles and valid prerequisites.")

    # 2. Test Curated GOAT Video Service
    resolved_html = resolve_topic_videos(
        "fs_topic_html_css", "Semantic HTML & CSS", "frontend",
        {"experience_level": "beginner", "learning_style": "visual", "language_preference": "english"}
    )
    assert len(resolved_html["all_lectures"]) >= 2
    assert resolved_html["recommended_lecture"] is not None
    assert "Kevin Powell" in resolved_html["recommended_lecture"]["provider"] or "freeCodeCamp" in resolved_html["recommended_lecture"]["provider"]
    assert "mU6anWqZJcc" not in resolved_html["recommended_lecture"]["video_url"] # Verify hardcoded link is gone!
    print(f"[PASS] Curated GOAT video resolved for HTML/CSS: Provider='{resolved_html['recommended_lecture']['provider']}' | Match='{resolved_html['match_reason']}'")

    # Test Hinglish personalization preference
    resolved_hinglish = resolve_topic_videos(
        "fs_topic_js_es6", "JavaScript Async & Promises", "frontend",
        {"experience_level": "intermediate", "learning_style": "visual", "language_preference": "hinglish"}
    )
    providers = [l["provider"] for l in resolved_hinglish["all_lectures"]]
    assert any("Akshay Saini" in p or "Chai aur Code" in p for p in providers)
    print(f"[PASS] Hinglish GOAT video matched: Options include {[l['provider'] for l in resolved_hinglish['all_lectures']]}")

    # 3. Test Prerequisite Checker & State Transitions
    test_profile = PersonalizationEngine.initialize_learner_profile("test_u1", "u1@test.dev", "Test Learner")
    
    # skill_react_architecture depends on skill_async_js, which depends on skill_javascript_core
    satisfied, missing = PersonalizationEngine.check_prerequisites_satisfied("skill_react_architecture", test_profile["skill_states"])
    assert satisfied is False
    assert "skill_async_js" in missing
    print(f"[PASS] Prerequisite engine correctly blocked advanced React before Async JS foundations: Missing={missing}")

    # Upgrade async js
    PersonalizationEngine.update_skill_evidence(test_profile, "skill_html_css", "lab", success=True)
    PersonalizationEngine.update_skill_evidence(test_profile, "skill_javascript_core", "lab", success=True)
    PersonalizationEngine.update_skill_evidence(test_profile, "skill_async_js", "lab", success=True)

    satisfied_now, missing_now = PersonalizationEngine.check_prerequisites_satisfied("skill_react_architecture", test_profile["skill_states"])
    assert satisfied_now is True
    print("[PASS] Prerequisite engine unlocked React once prerequisites were demonstrated.")

    # Test weak skill triggers targeted revision
    PersonalizationEngine.update_skill_evidence(test_profile, "skill_javascript_core", "quiz", success=False, score_pct=30.0, hints_used=3)
    assert test_profile["skill_states"]["skill_javascript_core"]["state"] == "needs_revision"
    
    mission = PersonalizationEngine.select_next_recommended_mission(test_profile)
    assert mission["mission_type"] == "targeted_revision"
    assert mission["skill_id"] == "skill_javascript_core"
    print(f"[PASS] Adaptive replanning generated targeted revision mission for weak skill: '{mission['title']}'")

    # 4. HTTP API End-to-End Testing with AsyncClient
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as client:
        # Register user with unique timestamped email
        unique_email = f"pers_test_{int(asyncio.get_event_loop().time())}@horizon.dev"
        reg_res = await client.post("/api/auth/register", json={
            "email": unique_email,
            "password": "Password123!",
            "full_name": "Personalization Tester"
        })
        auth_data = reg_res.json()
        token = auth_data["access_token"]
        headers = {"Authorization": f"Bearer {token}"}


        # GET /api/personalization/profile
        res = await client.get("/api/personalization/profile", headers=headers)
        assert res.status_code == 200
        p_data = res.json()
        assert p_data["user_id"] is not None
        print("[PASS] GET /api/personalization/profile passed.")

        # POST /api/personalization/onboarding
        res = await client.post("/api/personalization/onboarding", json={
            "career_certainty": "exploring_options",
            "activity_interests": ["building_websites", "analyzing_data"],
            "experience_level": "beginner",
            "weekly_hours": 15,
            "planning_horizon": "3_months",
            "learning_style": "visual",
            "language_preference": "both",
            "target_career": "fullstack"
        }, headers=headers)
        assert res.status_code == 200
        assert res.json()["domain"] == "fullstack"
        assert len(res.json()["milestones"]) >= 3
        print(f"[PASS] POST /api/personalization/onboarding passed: Calibrated {res.json()['domain']} for 3_months at 15 hrs/wk.")

        # GET /api/personalization/exploration
        res = await client.get("/api/personalization/exploration")
        assert res.status_code == 200
        acts = res.json()["activities"]
        assert len(acts) >= 5
        print(f"[PASS] GET /api/personalization/exploration passed: {len(acts)} activities available.")

        # POST /api/personalization/exploration/feedback
        res = await client.post("/api/personalization/exploration/feedback", json={
            "activity_id": "exp_frontend_interactive",
            "domain": "frontend",
            "interest_rating": 5,
            "difficulty_rating": 2,
            "would_explore_further": True,
            "completed_independently": True,
            "confusing_part": "None, counter glow was super rewarding!"
        }, headers=headers)
        assert res.status_code == 200
        assert res.json()["ranking"]["top_domain"] is not None
        print(f"[PASS] POST /api/personalization/exploration/feedback passed: Empirical evidence updated top domain to {res.json()['ranking']['top_domain']}.")

        # GET /api/personalization/missions/next
        res = await client.get("/api/personalization/missions/next", headers=headers)
        assert res.status_code == 200
        msn_data = res.json()["mission"]
        assert msn_data["id"] is not None
        assert msn_data["learn_module"] is not None
        assert msn_data["practice_module"] is not None
        assert msn_data["prove_module"] is not None
        print(f"[PASS] GET /api/personalization/missions/next passed: 3-part mission '{msn_data['title']}' (~{msn_data['estimated_minutes']} mins).")

        # POST /api/personalization/missions/{id}/complete
        res = await client.post(f"/api/personalization/missions/{msn_data['id']}/complete", json={
            "skill_id": msn_data["skill_id"],
            "success": True
        }, headers=headers)
        assert res.status_code == 200
        assert res.json()["awarded_xp"] == 50
        print(f"[PASS] POST /api/personalization/missions/{msn_data['id']}/complete passed: Skill state updated to {res.json()['skill_update']['new_state']}.")

        # POST /api/topics/{topic_id}/select-video
        res = await client.post("/api/topics/fs_topic_html_css/select-video", json={
            "video_id": "vid_chai_html_css"
        }, headers=headers)
        assert res.status_code == 200
        assert res.json()["selected_video_id"] == "vid_chai_html_css"
        print("[PASS] POST /api/topics/fs_topic_html_css/select-video passed: Preference saved to database.")

        # Verify topic returns Chai aur Code as active/recommended now!
        res = await client.get("/api/topics/fs_topic_html_css", headers=headers)
        assert res.status_code == 200
        topic_payload = res.json()
        assert topic_payload["topic"]["recommended_lecture"]["id"] == "vid_chai_html_css"
        assert "Chai aur Code" in topic_payload["topic"]["recommended_lecture"]["provider"]
        print(f"[PASS] User video preference persisted across calls: '{topic_payload['topic']['recommended_lecture']['title']}'")

        # POST /api/personalization/planning
        res = await client.post("/api/personalization/planning", json={
            "planning_horizon": "1_year",
            "weekly_hours": 20
        }, headers=headers)
        assert res.status_code == 200
        assert res.json()["planning_horizon"] == "1_year"
        print("[PASS] POST /api/personalization/planning passed: Adjusted to 1_year at 20 hrs/wk.")

        # GET /api/personalization/journey
        res = await client.get("/api/personalization/journey", headers=headers)
        assert res.status_code == 200
        j_data = res.json()
        assert len(j_data["milestones"]) >= 3
        print(f"[PASS] GET /api/personalization/journey passed: {len(j_data['milestones'])} milestones rendered.")

        # POST /api/personalization/explain-skill
        res = await client.post("/api/personalization/explain-skill", json={
            "career_goal": "fullstack",
            "skill_name": "Asynchronous JavaScript",
            "user_style": "visual",
            "user_level": "beginner"
        })
        assert res.status_code == 200
        assert len(res.json()["explanation"]) > 20
        print(f"[PASS] POST /api/personalization/explain-skill passed: Explanation='{res.json()['explanation'][:60]}...'")

    print("\n=== ALL ADAPTIVE PERSONALIZATION & GOAT VIDEO TESTS PASSED WITH 100% SUCCESS ===")


if __name__ == "__main__":
    asyncio.run(run_personalization_tests())
