# Project Horizon - Development & Execution Memory

## Overview
Horizon is an AI-powered next-generation learning platform unifying adaptive career roadmaps, interactive code labs, and gamified mastery loops into a seamless single destination.

## Key Platform Flow
1. **Landing Page**: Modern high-conversion entry with instant Login / Signup modal.
2. **15-Question Psychological Diagnostic Onboarding (Fresher-Friendly)**:
   - Eliminates technical jargon (no Docker, Kubernetes, linear algebra).
   - Grounded in real-world psychology: daily satisfaction triggers, reaction to frustration, visual vs logic orientation, gaming roles, and the classic *"started 4 languages and quit"* trap.
   - **IDK Option ("🤔 I don't know / Not sure yet")** on every question: Users who don't know are never penalized or forced into a rigid box.
   - **The Curious Explorer Track**: Automatically arranged for uncertain freshers with gentle gateway foundations.
3. **In-Learning Adaptive Reflections (Dynamic Career Calibration)**:
   - As users complete lectures or hands-on labs, 5-second contextual reflection prompts appear (e.g. *"You just wrote styling code. How did that feel? Did your brain love the visual tweak, or are you craving deep logic?"*).
   - Dynamically adapts their roadmap and career compass over time!
4. **Personalized Dashboard**:
   - **Top 4 Curated Roadmaps** customized to psychological archetype (e.g. The Visual Craftsman, The Systems Detective, The All-Rounder Creator, The Curious Explorer).
   - **"See All Courses"** master library across all tech domains with search and category filters.
5. **Unified Learning Workspace**:
   - 📺 **Lectures** (Expert curated masterclass video lectures)
   - 📝 **Notes** (Deep conceptual notes & code examples)
   - ❓ **Questions** (Instant interactive quizzes with XP)
   - 💻 **Labs** (In-browser coding exercises with live validation)
   - 🛠️ **Workshops** (Step-by-step capstone project builds)
6. **Persistence & Gamification**:
   - MongoDB database storing user profiles, assessment logs, roadmap milestones, and granular progress.
   - Streaks, XP system, level progression, and badge achievements.

## Architecture
- **Frontend**: Next.js 16 App Router (React 19, Tailwind CSS, Lucide Icons, Canvas Confetti)
- **Backend**: FastAPI (Python 3.12), Uvicorn, Pydantic, Motor / PyMongo with robust document store persistence
- **Database**: MongoDB (with seamless fallback persistence engine ensuring zero setup blockers)

## Execution History & Status Log
- [x] **Phase 1: System Blueprint & Workspace Scaffolding**: FastAPI backend venv created, Next.js frontend scaffolded, dependencies installed (`fastapi`, `uvicorn`, `motor`, `pymongo`, `bcrypt`, `lucide-react`, `canvas-confetti`).
- [x] **Phase 2: Content Aggregation & Curation Engine**: 6 comprehensive roadmaps with stages, 15 psychological diagnostic questions, and rich topic modules created in `backend/data/`.
- [x] **Phase 3: Database & Document Persistence Layer**: MongoDB Motor integration + robust document persistence fallback engine created in `backend/database.py`.
- [x] **Phase 4: Psychological Assessment & Archetype Engine**: Re-architected with 15 non-technical psychological questions, universal IDK options, and adaptive checkpoint reflections in `backend/data/assessment_questions.py` and `backend/scoring.py`.
- [x] **Phase 5: FastAPI Backend Core & Auth API**: REST API with JWT, 15-Q assessment submit, adaptive checkpoints, top 4 roadmaps, and lab test runner. All tests verified in `backend/test_backend.py`.
- [x] **Phase 6: Next.js Frontend - Design System & High-Converting Landing Page**: Established glassmorphic dark theme, `Navbar.tsx`, `AuthModal.tsx`, and `LandingHero.tsx`.
- [x] **Phase 7: Interactive Psychological Onboarding Flow**: Updated `AssessmentWizard.tsx` with friendly IDK card styling, psychological category badges, archetype reveal, and compassionate Curious Explorer onboarding.
- [x] **Phase 8: Personalized Dashboard & Top 4 Roadmaps + See All Courses**: Built `DashboardView.tsx` with Archetype HUD badge, adaptive track indicator, and filterable master explorer.
- [x] **Phase 9: Deep Learning Workspace with In-Learning Checkpoints**: Built `TopicWorkspace.tsx` with 5 learning modes + live **"🧠 Adaptive Career Compass"** in-learning reflection check-ins.
- [x] **Phase 10: End-to-End Integration, Gamification Polish, Testing & Launch**: Next.js production build succeeded (`npm run build`), `start.bat` and `start.ps1` launch scripts created, 100% verified.
