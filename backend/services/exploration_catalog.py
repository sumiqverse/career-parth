"""
Practical Career Exploration Activities Catalog.
Enables learners who are unsure about their career to try short, beginner-friendly 15-20 minute
practical activities across domains (Frontend, Backend, AI/ML, DevOps, Cyber Security, Android)
and submit qualitative feedback to adjust their career recommendation ranking with real evidence.
"""

from typing import Dict, Any, List

EXPLORATION_ACTIVITIES: List[Dict[str, Any]] = [
    {
        "id": "exp_frontend_interactive",
        "domain": "frontend",
        "title": "Interactive UI: Build a Live Glowing Button & Counter",
        "tagline": "Craft a reactive web interface that responds to user clicks instantly",
        "duration_mins": 20,
        "difficulty": "Beginner Friendly",
        "skills_tested": ["HTML DOM", "CSS Styling", "Event Listeners"],
        "instructions": (
            "1. Inspect the card structure with a heading, counter badge, and interactive button.\n"
            "2. Write a click event listener in JavaScript that increments the count and toggles a neon glow class.\n"
            "3. Observe how instant visual feedback makes digital interfaces feel alive."
        ),
        "starter_code": (
            "// 1. Select the button and counter elements\n"
            "const btn = document.querySelector('#boost-btn');\n"
            "const countBadge = document.querySelector('#count');\n"
            "let count = 0;\n\n"
            "btn.addEventListener('click', () => {\n"
            "  count += 1;\n"
            "  countBadge.textContent = count;\n"
            "  btn.classList.add('glow');\n"
            "});"
        ),
        "expected_concept": "Event handling & DOM reactivity",
        "test_criterion": "addEventListener",
        "reflection_prompts": [
            "Did you enjoy seeing visual changes on the screen immediately?",
            "Did designing interface layouts feel exciting or tedious?"
        ]
    },
    {
        "id": "exp_backend_api_route",
        "domain": "backend",
        "title": "API Architect: Build a Secure JSON Endpoint with Filtering",
        "tagline": "Design the server logic that powers web applications behind the scenes",
        "duration_mins": 20,
        "difficulty": "Beginner Friendly",
        "skills_tested": ["HTTP Methods", "RESTful Routes", "JSON Serialization"],
        "instructions": (
            "1. Review how clients send GET requests to a server endpoint.\n"
            "2. Define an async FastAPI route @app.get('/api/users') that accepts an optional 'status' query filter.\n"
            "3. Return clean JSON data with HTTP 200 status code."
        ),
        "starter_code": (
            "from fastapi import FastAPI, Query\n"
            "app = FastAPI()\n\n"
            "@app.get('/api/users')\n"
            "async def get_users(role: str = Query('developer')):\n"
            "    # Filter and return JSON response\n"
            "    return {\n"
            "        'status': 'success',\n"
            "        'filtered_role': role,\n"
            "        'count': 1\n"
            "    }"
        ),
        "expected_concept": "Request-response cycle & route parameters",
        "test_criterion": "get_users",
        "reflection_prompts": [
            "Did structuring data pipelines and server endpoints feel logical?",
            "Do you prefer working on hidden backend engine architecture over visual graphics?"
        ]
    },
    {
        "id": "exp_aiml_classifier",
        "domain": "ai_ml",
        "title": "Machine Learning Lab: Predict Customer Churn with Scikit-Learn",
        "tagline": "Train a decision model to discover patterns in raw numerical data",
        "duration_mins": 20,
        "difficulty": "Beginner Friendly",
        "skills_tested": ["Feature Arrays", "Train/Test Split", "Model Evaluation"],
        "instructions": (
            "1. Load a tabular dataset of customer usage metrics.\n"
            "2. Train a DecisionTreeClassifier on training features (X_train, y_train).\n"
            "3. Evaluate the model accuracy score and inspect which features drove the prediction."
        ),
        "starter_code": (
            "from sklearn.tree import DecisionTreeClassifier\n"
            "from sklearn.metrics import accuracy_score\n\n"
            "def train_churn_model(X_train, y_train, X_test, y_test):\n"
            "    clf = DecisionTreeClassifier(max_depth=3)\n"
            "    clf.fit(X_train, y_train)\n"
            "    preds = clf.predict(X_test)\n"
            "    return accuracy_score(y_test, preds)"
        ),
        "expected_concept": "Pattern recognition & mathematical decision boundaries",
        "test_criterion": "fit",
        "reflection_prompts": [
            "Did finding mathematical patterns in data excite you?",
            "Are you comfortable with statistics and probabilistic outcomes?"
        ]
    },
    {
        "id": "exp_devops_docker_deploy",
        "domain": "devops",
        "title": "Cloud Engineer: Package & Containerize an Application",
        "tagline": "Ensure applications run reliably anywhere in isolated container environments",
        "duration_mins": 20,
        "difficulty": "Beginner Friendly",
        "skills_tested": ["Dockerfile Syntax", "Port Mapping", "Environment Isolation"],
        "instructions": (
            "1. Create a minimal Dockerfile specifying base image, working directory, and dependencies.\n"
            "2. Copy source code and expose application port 8000.\n"
            "3. Define the container startup entrypoint command."
        ),
        "starter_code": (
            "FROM python:3.12-slim\n"
            "WORKDIR /app\n"
            "COPY requirements.txt .\n"
            "RUN pip install --no-cache-dir -r requirements.txt\n"
            "COPY . .\n"
            "EXPOSE 8000\n"
            "CMD [\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]"
        ),
        "expected_concept": "Linux process isolation & automated deployments",
        "test_criterion": "WORKDIR",
        "reflection_prompts": [
            "Do you like automating deployment pipelines and infrastructure?",
            "Does keeping systems highly reliable and scalable sound rewarding?"
        ]
    },
    {
        "id": "exp_cyber_auth_audit",
        "domain": "cybersecurity",
        "title": "Security Guard: Prevent SQL Injection in Auth Query",
        "tagline": "Discover how hackers bypass login screens and patch vulnerability holes",
        "duration_mins": 20,
        "difficulty": "Beginner Friendly",
        "skills_tested": ["Vulnerability Discovery", "Parameterized Queries", "Input Sanitization"],
        "instructions": (
            "1. Inspect an insecure dynamic SQL string concatenation: f\"SELECT * FROM users WHERE email='{input}'\"\n"
            "2. Observe how entering \"' OR '1'='1\" bypasses authentication completely!\n"
            "3. Refactor the code to use parameterized queries with safe placeholder parameters."
        ),
        "starter_code": (
            "# Insecure: query = f\"SELECT * FROM users WHERE email='{user_input}'\"\n"
            "# Secure fix with parameterization:\n"
            "def safe_login_query(cursor, email, password_hash):\n"
            "    query = \"SELECT id, email FROM users WHERE email = %s AND password_hash = %s\"\n"
            "    cursor.execute(query, (email, password_hash))\n"
            "    return cursor.fetchone()"
        ),
        "expected_concept": "Threat modeling & defensive validation",
        "test_criterion": "safe_login_query",
        "reflection_prompts": [
            "Did finding security flaws and thinking like an attacker captivate you?",
            "Do you enjoy investigating system vulnerabilities and encrypting sensitive data?"
        ]
    }
]


def get_exploration_activities(domain_filter: str = None) -> List[Dict[str, Any]]:
    if not domain_filter or domain_filter == "all":
        return EXPLORATION_ACTIVITIES
    return [act for act in EXPLORATION_ACTIVITIES if act.get("domain") == domain_filter]


def calculate_career_ranking_with_evidence(
    base_scores: Dict[str, float],
    exploration_history: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Combines initial assessment scores with real empirical evidence from completed exploration tasks.
    Weighting rule:
    - Base assessment interest provides preliminary heuristic (60% weight)
    - Practical exploration feedback (interest rating 1-5, difficulty comfort, would_explore_further) provides 40% weight.
    """
    updated_scores = dict(base_scores)

    for record in exploration_history:
        domain = record.get("domain")
        if not domain or domain not in updated_scores:
            continue

        interest_rating = float(record.get("interest_rating", 3)) # 1 to 5
        difficulty_rating = float(record.get("difficulty_rating", 3)) # 1 to 5
        would_explore = bool(record.get("would_explore_further", True))
        independent = bool(record.get("completed_independently", True))

        # Evidence delta calculation
        interest_delta = (interest_rating - 3.0) * 8.0 # -16 to +16
        explore_bonus = 6.0 if would_explore else -8.0
        independence_bonus = 4.0 if independent else 1.0

        total_adjustment = interest_delta + explore_bonus + independence_bonus
        updated_scores[domain] = max(5.0, min(100.0, updated_scores[domain] + total_adjustment))

    # Normalize ranking
    ranked_domains = sorted(updated_scores.items(), key=lambda x: x[1], reverse=True)

    return {
        "updated_scores": {k: round(v, 1) for k, v in ranked_domains},
        "top_domain": ranked_domains[0][0] if ranked_domains else "fullstack",
        "evidence_count": len(exploration_history)
    }
