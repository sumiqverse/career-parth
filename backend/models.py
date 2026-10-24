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
    description: str
    domain_scores: Dict[str, int]
    top_roadmaps: List[Dict[str, Any]]

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
    source_attribution: str = "Synthesized from roadmap.sh, freeCodeCamp, and Boot.dev"

# --- Deep Topic Content Models ---
class Lecture(BaseModel):
    id: str
    title: str
    provider: str # freeCodeCamp / Boot.dev / Horizon Expert
    video_url: str
    duration: str
    summary: str
    key_takeaways: List[str]

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
