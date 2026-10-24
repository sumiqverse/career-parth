@echo off
TITLE Horizon Learning Platform Launcher
echo ========================================================
echo         HORIZON - AI-POWERED LEARNING EXPERIENCE
echo    Adaptive Paths, Interactive Labs, and Mastery Loops
echo ========================================================
echo.

echo [1/2] Starting FastAPI Backend on http://localhost:8000 ...
start "Horizon Backend (FastAPI)" cmd /k "cd backend && venv\Scripts\python.exe -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

echo [2/2] Starting Next.js Frontend on http://localhost:3000 ...
start "Horizon Frontend (Next.js)" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================================
echo Both servers are launching!
echo Backend API Docs:   http://localhost:8000/docs
echo Frontend Web App:   http://localhost:3000
echo ========================================================
echo.
pause
