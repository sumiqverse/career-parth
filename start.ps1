Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "        HORIZON - AI-POWERED LEARNING EXPERIENCE        " -ForegroundColor Yellow
Write-Host "    Synthesizing roadmap.sh, freeCodeCamp, and Boot.dev " -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

$workspace = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "[1/2] Starting FastAPI Backend on http://localhost:8000 ..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$workspace\backend'; .\venv\Scripts\python.exe -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

Write-Host "[2/2] Starting Next.js Frontend on http://localhost:3000 ..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$workspace\frontend'; npm run dev"

Write-Host ""
Write-Host "========================================================" -ForegroundColor Green
Write-Host "Both services are running in separate windows:" -ForegroundColor White
Write-Host "Frontend Application: http://localhost:3000" -ForegroundColor Yellow
Write-Host "Backend API Swagger:  http://localhost:8000/docs" -ForegroundColor Yellow
Write-Host "========================================================" -ForegroundColor Green
