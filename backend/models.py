from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime

# --- Auth Models ---
class UserRegister(BaseModel):
    email: str
    password: str
    full_name: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserProfile(BaseModel):
    id: str
    email: str
    full_name: str
    avatar: Optional[str] = None
    created_at: str
    primary_domain: Optional[str] = None
    xp: int = 0
    streak: int = 1
    level: int = 1
    badges: List[str] = []

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserProfile

# --- Assessment Models ---
class QuestionOption(BaseModel):
    id: str
    text: str
    domain_scores: Dict[str, int] # e.g. {"frontend": 3, "fullstack": 2}
    is_idk: Optional[bool] = False

class AssessmentQuestion(BaseModel):
    id: int
    question: str
    category: str
    options: List[QuestionOption]

class AssessmentSubmitRequest(BaseModel):
    answers: Dict[str, str] # question_id (as str) -> option_id

class AssessmentResultResponse(BaseModel):
    recommended_domain: str
    domain_display_name: str
    archetype: Optional[str] = None
    tagline: Optional[str] = None
    description: str
    why_it_fits: Optional[str] = None
    idk_count: int = 0
    is_exploring_mode: bool = False
    domain_scores: Dict[str, int]
    top_roadmaps: List[Dict[str, Any]]

class AdaptiveReflectionSubmit(BaseModel):
    checkpoint_id: str
    topic_id: str
    selected_option_id: str
    reinforce_domain: str

# --- Roadmap & Course Models ---
class TopicSummary(BaseModel):
    id: str
    title: str
    description: str
    duration_mins: int
    xp: int
    is_completed: bool = False

class Stage(BaseModel):
    id: str
    order: int
    title: str
    description: str
    topics: List[TopicSummary]

class Roadmap(BaseModel):
    id: str
    slug: str
    title: str
    tagline: str
    description: str
    domain: str
    icon: str
    gradient: str
    difficulty: str # Beginner, Intermediate, Advanced
    estimated_hours: int
    total_xp: int
    stages: List[Stage]
    source_attribution: str = "Industry Standard Curriculum"

# --- Deep Topic Content Models ---
class Lecture(BaseModel):
    id: str
    title: str
    provider: str = "Horizon Masterclass"
    video_url: str
    duration: str
    summary: str
    key_takeaways: List[str]
    style: Optional[str] = "comprehensive_masterclass" # fastpaced_visual, architectural_deepdive, hinglish_regional
    creator_type: Optional[str] = "global_goat" # global_goat, hinglish_goat
    rating: Optional[float] = 4.95
    view_count: Optional[str] = "1M+ views"
    level: Optional[str] = "beginner"
    is_recommended: Optional[bool] = False
    match_reason: Optional[str] = None

class QuizQuestion(BaseModel):
    id: str
    question: str
    options: List[str]
    correct_option: int
    explanation: str
    xp: int = 25

class LabChallenge(BaseModel):
    id: str
    title: str
    instructions: str
    language: str # javascript, python, html, sql
    starter_code: str
    test_cases: List[Dict[str, Any]] # input, expected, description
    hint: str
    xp: int = 50

class WorkshopGuide(BaseModel):
    id: str
    title: str
    tagline: str
    overview: str
    steps: List[str]
    starter_repo_url: Optional[str] = None
    acceptance_criteria: List[str]
    xp: int = 100

class TopicDetail(BaseModel):
    id: str
    roadmap_slug: str
    stage_id: str
    title: str
    description: str
    lectures: List[Lecture]
    notes: str # Rich markdown
    questions: List[QuizQuestion]
    lab: LabChallenge
    workshop: WorkshopGuide

# --- User Progress Models ---
class ProgressUpdateRequest(BaseModel):
    roadmap_slug: str
    topic_id: str
    action_type: str # "lecture", "note", "quiz", "lab", "workshop", "topic_complete"
    score: Optional[int] = None
    code_submission: Optional[str] = None

class GamificationStatus(BaseModel):
    xp: int
    streak: int
    level: int
    next_level_xp: int
    progress_percentage: float
    badges: List[Dict[str, Any]]
    completed_topics_count: int

# --- Personalization & Learner Model Request/Response Models ---
class OnboardingRequest(BaseModel):
    career_certainty: Optional[str] = "exploring_options" # specific_goal, exploring_options, unsure
    activity_interests: Optional[List[str]] = []
    experience_level: Optional[str] = "beginner" # beginner, intermediate, advanced
    weekly_hours: Optional[int] = 10
    planning_horizon: Optional[str] = "6_months" # 1_month, 3_months, 6_months, 1_year, 4_years
    learning_style: Optional[str] = "visual" # visual, comprehensive
    language_preference: Optional[str] = "both" # english, hinglish, both
    target_career: Optional[str] = None

class ExplorationFeedbackRequest(BaseModel):
    activity_id: str
    domain: str
    interest_rating: int # 1 to 5
    difficulty_rating: int # 1 to 5
    would_explore_further: bool
    completed_independently: bool
    confusing_part: Optional[str] = None

class PlanningUpdateRequest(BaseModel):
    planning_horizon: str # 1_month, 3_months, 6_months, 1_year, 4_years
    weekly_hours: int

class SelectVideoRequest(BaseModel):
    video_id: str

