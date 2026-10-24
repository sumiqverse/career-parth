# HORIZON: AI-Powered Unified Learning Platform

> Synthesizing the structured pathways of **roadmap.sh**, the hands-on project mastery of **freeCodeCamp.org**, and the addictive mastery loops of **Boot.dev**.

---

## 🌟 Key Architecture & Highlights

1. **Landing Page with Instant Auth**:
   - Modern glassmorphic dark mode UI.
   - Seamless Login & Registration modal with JWT token management and bcrypt password hashing.

2. **15-Question Diagnostic Onboarding**:
   - 15 questions mapping technical inclination, visual vs logic orientation, math comfort, problem solving, and career goals.
   - Evaluates scores across **Full Stack**, **Backend**, **AI/ML**, **Frontend**, **DevOps**, and **Cyber Security**.
   - Recommends the optimal domain with an engineering profile breakdown.

3. **Personalized Dashboard & Top 4 Roadmaps**:
   - Displays the **Top 4 personalized roadmaps** dynamically customized to the learner's assessment results.
   - **"See All Courses & Roadmaps"** master library with real-time search and domain filter pills.
   - Interactive stages and topic milestone explorer.

4. **Deep Learning Workspace (5 Learning Modes per Topic)**:
   - 📺 **Lectures**: Curated full video masterclasses from freeCodeCamp & Boot.dev with key takeaways checklist.
   - 📝 **Notes**: In-depth theoretical notes with syntax snippets and architectural diagrams.
   - ❓ **Questions**: Interactive multiple-choice conceptual quizzes with instant educational explanations.
   - 💻 **Labs**: In-browser interactive code editor with live test case runner and assertion console.
   - 🛠️ **Workshops**: Step-by-step capstone project builds with interactive progress checklists.

5. **Gamification & Cloud Persistence**:
   - MongoDB database (with resilient document store fallback ensuring zero runtime blockers).
   - Real-time progress synchronization: XP accumulation, level progression, daily streak preservation (🔥), and unlocked badges.

---

## 🚀 Quick Start Guide

### Option 1: One-Click Launch (Windows)
Double click `start.bat` in the root folder, or in PowerShell run:
```powershell
.\start.ps1
```

### Option 2: Manual Terminal Launch

#### Backend (FastAPI + MongoDB)
```powershell
cd backend
.\venv\Scripts\python.exe -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
*API documentation and Swagger UI*: [http://localhost:8000/docs](http://localhost:8000/docs)

#### Frontend (Next.js 16 + React 19 + Tailwind CSS)
```powershell
cd frontend
npm run dev
```
*Web Application*: [http://localhost:3000](http://localhost:3000)

---

## 🧪 Testing & Verification
To execute the automated backend test suite:
```powershell
.\backend\venv\Scripts\python.exe backend\test_backend.py
```

To execute the frontend production build verification:
```powershell
cd frontend
npm run build
```
