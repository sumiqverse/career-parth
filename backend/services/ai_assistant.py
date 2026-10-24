"""
Server-Side AI Assistance Layer for Horizon.
Provides context-aware explanations, conceptual simplifications, and hints
grounded in the learner's skill state and career goals.
Falls back safely to structured deterministic heuristics if no external AI API key is configured.
"""

import os
import json
import httpx
from typing import Dict, Any, Optional

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")


async def generate_learner_explanation(
    career_goal: str,
    skill_name: str,
    user_style: str = "visual",
    user_level: str = "beginner"
) -> Dict[str, Any]:
    """
    Generates a context-specific explanation for why a skill is vital for the learner's goal.
    """
    # Deterministic high-quality fallback explanation
    fallback_text = (
        f"In {career_goal.replace('_', ' ').title()}, mastering '{skill_name}' is essential. "
        f"At your {user_level} stage, developing strong mental models here directly unlocks "
        f"advanced system design and eliminates common development bottlenecks."
    )

    if GEMINI_API_KEY:
        try:
            async with httpx.AsyncClient(timeout=6.0) as client:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
                prompt = (
                    f"Explain why '{skill_name}' is critical for a {user_level} pursuing {career_goal}. "
                    f"Keep it under 3 concise sentences. The learner prefers a {user_style} learning style."
                )
                payload = {
                    "contents": [{"parts": [{"text": prompt}]}]
                }
                res = await client.post(url, json=payload)
                if res.status_code == 200:
                    data = res.json()
                    ai_text = data["candidates"][0]["content"]["parts"][0]["text"].strip()
                    return {
                        "explanation": ai_text,
                        "provider": "Gemini 1.5 Flash (AI Enhanced)",
                        "is_live_ai": True
                    }
        except Exception:
            pass

    return {
        "explanation": fallback_text,
        "provider": "Horizon Deterministic Guidance Engine",
        "is_live_ai": False
    }


async def generate_quiz_hint(
    question_text: str,
    concept: str
) -> Dict[str, Any]:
    """
    Generates a targeted hint without directly spoiling the correct answer.
    """
    fallback_hint = f"Focus on how '{concept}' controls program flow and memory isolation."
    
    return {
        "hint": fallback_hint,
        "provider": "Horizon Cognitive Support Engine",
        "is_live_ai": False
    }
