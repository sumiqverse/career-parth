import asyncio
import httpx
from main import app
from scoring import compute_assessment_result
from data.assessment_questions import ASSESSMENT_QUESTIONS
from data.seed_roadmaps import SEED_ROADMAPS, TOPIC_DETAILS

async def run_tests():
    print("=== STARTING HORIZON BACKEND VERIFICATION ===")
    
    # 1. Verify 15 Assessment Questions
    assert len(ASSESSMENT_QUESTIONS) == 15, f"Expected 15 questions, found {len(ASSESSMENT_QUESTIONS)}"
    print(f"[PASS] Assessment questions verified: {len(ASSESSMENT_QUESTIONS)} questions present.")

    # 2. Verify Seed Roadmaps
    assert len(SEED_ROADMAPS) >= 6, f"Expected at least 6 seed roadmaps, found {len(SEED_ROADMAPS)}"
    print(f"[PASS] Seed roadmaps verified: {len(SEED_ROADMAPS)} roadmaps present.")

    # 3. Verify Scoring Algorithm with different vectors
    test_answers_backend = {
        "1": "q1_b", "2": "q2_c", "3": "q3_b", "5": "q5_b",
        "7": "q7_d", "8": "q8_b", "10": "q10_b", "13": "q13_b"
    }
    result_be = compute_assessment_result(test_answers_backend)
    assert result_be["recommended_domain"] == "backend", f"Expected backend, got {result_be['recommended_domain']}"
    assert len(result_be["top_roadmaps"]) == 4, f"Expected 4 top roadmaps, got {len(result_be['top_roadmaps'])}"
    print(f"[PASS] Scoring test (Backend profile): Winner={result_be['recommended_domain']}, Top4 count={len(result_be['top_roadmaps'])}")

    test_answers_aiml = {
        "1": "q1_d", "3": "q3_c", "5": "q5_c", "6": "q6_c",
        "7": "q7_c", "8": "q8_c", "13": "q13_c", "15": "q15_c"
    }
    result_ai = compute_assessment_result(test_answers_aiml)
    assert result_ai["recommended_domain"] == "ai_ml", f"Expected ai_ml, got {result_ai['recommended_domain']}"
    print(f"[PASS] Scoring test (AI/ML profile): Winner={result_ai['recommended_domain']}, Top4 count={len(result_ai['top_roadmaps'])}")

    # 4. Verify IDK / Curious Explorer Mode
    test_answers_idk = {
        "1": "q1_idk", "2": "q2_idk", "3": "q3_idk", "4": "q4_idk",
        "5": "q5_idk", "6": "q6_idk", "7": "q7_idk"
    }
    result_idk = compute_assessment_result(test_answers_idk)
    assert result_idk["is_exploring_mode"] is True, "Expected is_exploring_mode to be True for multiple IDK answers"
    assert result_idk["archetype"] == "The Curious Explorer"
    print(f"[PASS] Scoring test (IDK / Curious Explorer profile): Archetype={result_idk['archetype']}, IDK count={result_idk['idk_count']}")

    # 5. In-process HTTP testing with AsyncClient
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as client:
        # Health check
        res = await client.get("/api/health")
        assert res.status_code == 200
        print("[PASS] GET /api/health passed.")

        # Assessment questions
        res = await client.get("/api/assessment/questions")
        assert res.status_code == 200
        data = res.json()
        assert data["total_questions"] == 15
        print("[PASS] GET /api/assessment/questions passed.")

        # Roadmaps Top 4
        res = await client.get("/api/roadmaps/top4")
        assert res.status_code == 200
        top4 = res.json()
        assert len(top4) == 4
        print(f"[PASS] GET /api/roadmaps/top4 passed: {[r['title'] for r in top4]}")

        # All Roadmaps
        res = await client.get("/api/roadmaps")
        assert res.status_code == 200
        all_rm = res.json()
        assert len(all_rm) >= 6
        print(f"[PASS] GET /api/roadmaps passed: {len(all_rm)} roadmaps found.")

        # Auth Registration
        unique_email = f"test_{int(asyncio.get_event_loop().time())}@horizon.dev"
        res = await client.post("/api/auth/register", json={
            "email": unique_email,
            "password": "Password123!",
            "full_name": "Antigravity Tester"
        })
        assert res.status_code == 200, f"Register failed: {res.text}"
        auth_data = res.json()
        token = auth_data["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        print("[PASS] POST /api/auth/register passed.")

        # Auth Login
        res = await client.post("/api/auth/login", json={
            "email": unique_email,
            "password": "Password123!"
        })
        assert res.status_code == 200
        print("[PASS] POST /api/auth/login passed.")

        # Auth Me
        res = await client.get("/api/auth/me", headers=headers)
        assert res.status_code == 200
        assert res.json()["email"] == unique_email
        print("[PASS] GET /api/auth/me passed.")

        # Submit Assessment
        res = await client.post("/api/assessment/submit", json={"answers": test_answers_aiml}, headers=headers)
        assert res.status_code == 200
        asmt_res = res.json()
        assert asmt_res["recommended_domain"] == "ai_ml"
        print(f"[PASS] POST /api/assessment/submit passed: Recommended domain = {asmt_res['recommended_domain']}")

        # Topic Detail
        res = await client.get("/api/topics/fs_topic_html_css", headers=headers)
        assert res.status_code == 200
        topic_payload = res.json()
        assert topic_payload["topic"]["title"] == "Semantic HTML & Modern Flexbox/Grid"
        assert len(topic_payload["topic"]["lectures"]) >= 1
        assert len(topic_payload["topic"]["questions"]) >= 1
        assert topic_payload["topic"]["lab"] is not None
        assert topic_payload["topic"]["workshop"] is not None
        print("[PASS] GET /api/topics/fs_topic_html_css (Lectures, Notes, Questions, Lab, Workshop) passed.")

        # Progress Completion
        res = await client.post("/api/progress/complete", json={
            "roadmap_slug": "full-stack-developer",
            "topic_id": "fs_topic_html_css",
            "action_type": "quiz"
        }, headers=headers)
        assert res.status_code == 200
        prog_res = res.json()
        assert "quiz" in prog_res["completed_items"]
        print(f"[PASS] POST /api/progress/complete passed: Awarded {prog_res['earned_xp']} XP.")

        # Gamification Status
        res = await client.get("/api/gamification/status", headers=headers)
        assert res.status_code == 200
        gam_res = res.json()
        assert gam_res["xp"] > 0
        assert gam_res["level"] >= 1
        print(f"[PASS] GET /api/gamification/status passed: XP={gam_res['xp']}, Level={gam_res['level']}, Badges={len(gam_res['badges'])}")

        # Lab Code Runner
        res = await client.post("/api/labs/run-code", json={
            "code": ".feature-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }",
            "test_cases": [
                {"expected": "display: grid", "description": "Uses grid"},
                {"expected": "minmax", "description": "Uses minmax"}
            ]
        })
        assert res.status_code == 200
        lab_res = res.json()
        assert lab_res["success"] is True
        print("[PASS] POST /api/labs/run-code passed: Test cases validated successfully.")

        # Adaptive Checkpoint & In-Learning Reflection
        res = await client.get("/api/assessment/adaptive-checkpoint/fs_topic_html_css")
        assert res.status_code == 200
        chk_res = res.json()
        assert chk_res["available"] is True
        print("[PASS] GET /api/assessment/adaptive-checkpoint/fs_topic_html_css passed.")

        res = await client.post("/api/assessment/adaptive-reflection", json={
            "checkpoint_id": "chk_html_visual",
            "topic_id": "fs_topic_html_css",
            "selected_option_id": "chk_1_loved",
            "reinforce_domain": "frontend"
        }, headers=headers)
        assert res.status_code == 200
        ref_res = res.json()
        assert ref_res["status"] == "success"
        print("[PASS] POST /api/assessment/adaptive-reflection passed.")

    print("=== ALL HORIZON BACKEND VERIFICATION CHECKS PASSED SUCCESSFULLY ===")

if __name__ == "__main__":
    asyncio.run(run_tests())
