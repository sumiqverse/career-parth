"""
Deterministic, Prerequisite-Aware Adaptive Personalization Engine.
Manages the canonical skill graph, prerequisite validation, persistent learner model,
evidence-based skill mastery updates (unassessed, developing, needs_revision, provisionally_mastered),
horizon planning (1m, 3m, 6m, 1y, 4y), and generates 3-part daily/weekly missions.
"""

import uuid
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple

# Canonical Skill Definitions with explicit Prerequisite dependencies
CANONICAL_SKILL_GRAPH: Dict[str, Dict[str, Any]] = {
    # Web & Frontend Core
    "skill_html_css": {
        "id": "skill_html_css",
        "name": "Semantic HTML & Responsive Layouts",
        "category": "frontend",
        "difficulty": "beginner",
        "prerequisites": [],
        "estimated_hours": 8,
        "description": "Semantic markup, CSS Flexbox, Grid, accessibility standards, and responsive design."
    },
    "skill_javascript_core": {
        "id": "skill_javascript_core",
        "name": "JavaScript Fundamentals & ES6+",
        "category": "frontend",
        "difficulty": "beginner",
        "prerequisites": ["skill_html_css"],
        "estimated_hours": 15,
        "description": "Variables, scope, functions, closures, array methods, and DOM manipulation."
    },
    "skill_async_js": {
        "id": "skill_async_js",
        "name": "Asynchronous JavaScript & Event Loop",
        "category": "frontend",
        "difficulty": "intermediate",
        "prerequisites": ["skill_javascript_core"],
        "estimated_hours": 10,
        "description": "Event Loop, Call Stack, Web APIs, Promises, async/await, and fetch data handling."
    },
    "skill_react_architecture": {
        "id": "skill_react_architecture",
        "name": "React Component Architecture & Hooks",
        "category": "frontend",
        "difficulty": "intermediate",
        "prerequisites": ["skill_async_js"],
        "estimated_hours": 20,
        "description": "Components, JSX, state, effect hooks, custom hooks, and component lifecycle."
    },
    "skill_nextjs_fullstack": {
        "id": "skill_nextjs_fullstack",
        "name": "Next.js App Router & Server Components",
        "category": "frontend",
        "difficulty": "advanced",
        "prerequisites": ["skill_react_architecture"],
        "estimated_hours": 20,
        "description": "Server vs Client Components, dynamic file routes, streaming Suspense, and SEO metadata."
    },
    "skill_tailwind_design": {
        "id": "skill_tailwind_design",
        "name": "Tailwind CSS & Design Tokens",
        "category": "frontend",
        "difficulty": "beginner",
        "prerequisites": ["skill_html_css"],
        "estimated_hours": 10,
        "description": "Design systems, utility classes, dark mode theming, and responsive components."
    },
    "skill_tanstack_query": {
        "id": "skill_tanstack_query",
        "name": "TanStack Query & Server State Management",
        "category": "frontend",
        "difficulty": "intermediate",
        "prerequisites": ["skill_react_architecture"],
        "estimated_hours": 12,
        "description": "Remote caching, deduplication, optimistic updates, and cache invalidation."
    },

    # Backend & Distributed Systems
    "skill_http_networking": {
        "id": "skill_http_networking",
        "name": "HTTP Protocols & Network Layers",
        "category": "backend",
        "difficulty": "beginner",
        "prerequisites": [],
        "estimated_hours": 10,
        "description": "TCP/IP, HTTP/1.1 vs HTTP/2/3, headers, status codes, and TLS certificates."
    },
    "skill_python_core": {
        "id": "skill_python_core",
        "name": "Python Language Foundations",
        "category": "backend",
        "difficulty": "beginner",
        "prerequisites": [],
        "estimated_hours": 12,
        "description": "Python data structures, object-oriented programming, modules, and type hinting."
    },
    "skill_fastapi_rest": {
        "id": "skill_fastapi_rest",
        "name": "FastAPI & RESTful API Architecture",
        "category": "backend",
        "difficulty": "intermediate",
        "prerequisites": ["skill_http_networking", "skill_python_core"],
        "estimated_hours": 18,
        "description": "Async endpoints, Pydantic type validation, dependency injection, and OpenAPI."
    },
    "skill_auth_security": {
        "id": "skill_auth_security",
        "name": "Authentication, JWT & Security",
        "category": "backend",
        "difficulty": "intermediate",
        "prerequisites": ["skill_fastapi_rest"],
        "estimated_hours": 14,
        "description": "Stateless JWT tokens, bcrypt password hashing, HttpOnly cookies, and RBAC guards."
    },
    "skill_sql_databases": {
        "id": "skill_sql_databases",
        "name": "Relational Databases & SQL Optimization",
        "category": "backend",
        "difficulty": "intermediate",
        "prerequisites": ["skill_http_networking"],
        "estimated_hours": 16,
        "description": "PostgreSQL, normalization, joins, transactions, B-Tree indexes, and EXPLAIN ANALYZE."
    },
    "skill_nosql_mongodb": {
        "id": "skill_nosql_mongodb",
        "name": "MongoDB & Document Databases",
        "category": "backend",
        "difficulty": "intermediate",
        "prerequisites": ["skill_http_networking"],
        "estimated_hours": 14,
        "description": "BSON collections, aggregation pipelines, schema embedding, and compound indexing."
    },
    "skill_redis_caching": {
        "id": "skill_redis_caching",
        "name": "Redis & In-Memory Caching Strategies",
        "category": "backend",
        "difficulty": "intermediate",
        "prerequisites": ["skill_fastapi_rest"],
        "estimated_hours": 10,
        "description": "Cache-aside, write-through, TTL eviction, rate limiters, and distributed locks."
    },
    "skill_message_queues": {
        "id": "skill_message_queues",
        "name": "Message Brokers & Asynchronous Queues",
        "category": "backend",
        "difficulty": "advanced",
        "prerequisites": ["skill_fastapi_rest", "skill_redis_caching"],
        "estimated_hours": 16,
        "description": "Kafka, RabbitMQ, Celery workers, event-driven decoupling, and idempotent consumers."
    },

    # DevOps & Infrastructure
    "skill_docker_containers": {
        "id": "skill_docker_containers",
        "name": "Docker & Container Engineering",
        "category": "devops",
        "difficulty": "beginner",
        "prerequisites": ["skill_http_networking"],
        "estimated_hours": 14,
        "description": "Multi-stage Dockerfiles, image layers, port binding, volumes, and Docker Compose."
    },
    "skill_kubernetes_orchestration": {
        "id": "skill_kubernetes_orchestration",
        "name": "Kubernetes Cluster Orchestration",
        "category": "devops",
        "difficulty": "advanced",
        "prerequisites": ["skill_docker_containers"],
        "estimated_hours": 22,
        "description": "Pods, Deployments, Services, Helm charts, Ingress, and horizontal autoscaling."
    },

    # AI & Machine Learning
    "skill_numpy_pandas": {
        "id": "skill_numpy_pandas",
        "name": "NumPy & Pandas Data Manipulation",
        "category": "ai_ml",
        "difficulty": "beginner",
        "prerequisites": ["skill_python_core"],
        "estimated_hours": 15,
        "description": "Vectorized math, array broadcasting, DataFrame filtering, missing data cleaning."
    },
    "skill_classical_ml": {
        "id": "skill_classical_ml",
        "name": "Classical Machine Learning (Scikit-Learn)",
        "category": "ai_ml",
        "difficulty": "intermediate",
        "prerequisites": ["skill_numpy_pandas"],
        "estimated_hours": 20,
        "description": "Supervised regression, classification, Decision Trees, Random Forests, and cross-validation."
    },
    "skill_pytorch_deep_learning": {
        "id": "skill_pytorch_deep_learning",
        "name": "PyTorch Neural Networks & Backprop",
        "category": "ai_ml",
        "difficulty": "advanced",
        "prerequisites": ["skill_classical_ml"],
        "estimated_hours": 25,
        "description": "Autograd, tensor computation, loss functions, optimizers, and neural training loops."
    },
    "skill_rag_vector_db": {
        "id": "skill_rag_vector_db",
        "name": "RAG, Vector Databases & LLMs",
        "category": "ai_ml",
        "difficulty": "advanced",
        "prerequisites": ["skill_pytorch_deep_learning"],
        "estimated_hours": 22,
        "description": "Document chunking, vector embeddings, similarity search, and generative agent chains."
    },

    # Cyber Security
    "skill_owasp_security": {
        "id": "skill_owasp_security",
        "name": "OWASP Top 10 Web Security & Defenses",
        "category": "cybersecurity",
        "difficulty": "intermediate",
        "prerequisites": ["skill_http_networking"],
        "estimated_hours": 18,
        "description": "SQL Injection, XSS, CSRF, broken access control, and defensive hardening."
    }
}


def validate_canonical_graph() -> Tuple[bool, List[str]]:
    """
    Validates that CANONICAL_SKILL_GRAPH has no dangling prerequisites and no cyclic dependencies.
    """
    errors = []
    # 1. Check missing prerequisite IDs
    for skill_id, skill in CANONICAL_SKILL_GRAPH.items():
        for prereq in skill.get("prerequisites", []):
            if prereq not in CANONICAL_SKILL_GRAPH:
                errors.append(f"Skill {skill_id} references non-existent prerequisite: {prereq}")

    # 2. Cycle detection via DFS
    visited = {} # 0: unvisited, 1: visiting, 2: visited
    
    def dfs(s_id):
        visited[s_id] = 1
        for p_id in CANONICAL_SKILL_GRAPH[s_id].get("prerequisites", []):
            if p_id in CANONICAL_SKILL_GRAPH:
                if visited.get(p_id) == 1:
                    errors.append(f"Cycle detected involving prerequisite {p_id} -> {s_id}")
                    return True
                elif visited.get(p_id) == 0:
                    if dfs(p_id):
                        return True
        visited[s_id] = 2
        return False

    for s_id in CANONICAL_SKILL_GRAPH:
        visited[s_id] = 0
    for s_id in CANONICAL_SKILL_GRAPH:
        if visited[s_id] == 0:
            dfs(s_id)

    return len(errors) == 0, errors


class PersonalizationEngine:
    """
    Main algorithmic engine for learner state tracking, prerequisite verification,
    horizon pacing, and next-mission generation.
    """

    @staticmethod
    def initialize_learner_profile(user_id: str, email: str, full_name: str) -> Dict[str, Any]:
        """
        Creates a clean, production-ready persistent learner profile.
        """
        now = datetime.utcnow().isoformat()
        return {
            "id": f"lp_{user_id}",
            "user_id": user_id,
            "email": email,
            "full_name": full_name,
            "created_at": now,
            "updated_at": now,
            "onboarding": {
                "career_certainty": "exploring_options", # specific_goal, exploring_options, unsure
                "activity_interests": ["building_websites", "problem_solving"],
                "experience_level": "beginner", # beginner, intermediate, advanced
                "weekly_hours": 10, # 5, 10, 15, 20
                "planning_horizon": "6_months", # 1_month, 3_months, 6_months, 1_year, 4_years
                "learning_style": "visual", # visual, comprehensive
                "language_preference": "both", # english, hinglish, both
                "notes": "Initialized default profile"
            },
            "career_goal": {
                "primary_domain": "fullstack",
                "alternative_domains": ["backend", "frontend"],
                "confidence": "moderate", # high, moderate, preliminary
                "match_reasons": ["Balanced interest in both visual client UI and server architectures"]
            },
            # Map of skill_id -> {state, confidence, attempts, last_evidence, updated_at}
            "skill_states": {
                skill_id: {
                    "skill_id": skill_id,
                    "state": "unassessed", # unassessed, developing, needs_revision, provisionally_mastered
                    "confidence": 0.0,
                    "attempts": 0,
                    "last_evidence": None,
                    "updated_at": now
                }
                for skill_id in CANONICAL_SKILL_GRAPH
            },
            "exploration_history": [],
            "missions": [],
            "active_mission": None,
            "milestone_history": [
                {
                    "title": "Onboarding & Career Calibration",
                    "status": "completed",
                    "timestamp": now,
                    "reason": "Profile initiated"
                }
            ]
        }

    @staticmethod
    def update_skill_evidence(
        learner_profile: Dict[str, Any],
        skill_id: str,
        evidence_type: str, # "quiz", "lab", "exploration", "self_report"
        success: bool,
        score_pct: float = 100.0,
        hints_used: int = 0
    ) -> Dict[str, Any]:
        """
        Updates a specific skill's mastery state based on deterministic rules:
        - Quiz pass (> 70%): elevates to developing (or provisionally_mastered if already developing)
        - Quiz fail (< 50%): transitions to needs_revision
        - Lab pass without excessive hints: confirms provisionally_mastered
        - Lab fail: triggers needs_revision
        - Preserves previous strong evidence, does not instantly collapse score on a single minor mistake.
        """
        states = learner_profile.get("skill_states", {})
        if skill_id not in states:
            states[skill_id] = {
                "skill_id": skill_id,
                "state": "unassessed",
                "confidence": 0.0,
                "attempts": 0,
                "last_evidence": None,
                "updated_at": datetime.utcnow().isoformat()
            }

        skill_record = states[skill_id]
        prev_state = skill_record.get("state", "unassessed")
        prev_conf = skill_record.get("confidence", 0.0)
        attempts = skill_record.get("attempts", 0) + 1
        now = datetime.utcnow().isoformat()

        new_state = prev_state
        new_conf = prev_conf
        change_reason = ""

        if success:
            if evidence_type == "lab":
                new_state = "provisionally_mastered"
                new_conf = min(1.0, prev_conf + 0.35)
                change_reason = "Demonstrated independent execution in practical coding lab"
            elif evidence_type == "quiz":
                if prev_state in ["unassessed", "needs_revision"]:
                    new_state = "developing"
                    new_conf = min(1.0, prev_conf + 0.25)
                    change_reason = "Successfully passed conceptual validation quiz"
                elif prev_state == "developing" and attempts >= 2:
                    new_state = "provisionally_mastered"
                    new_conf = min(1.0, prev_conf + 0.30)
                    change_reason = "Consistent success across multiple assessments"
                else:
                    new_conf = min(1.0, prev_conf + 0.15)
            elif evidence_type == "exploration":
                new_state = "developing"
                new_conf = 0.4
                change_reason = "Completed beginner exploration experiment"
        else:
            # Failed attempt
            if hints_used > 2 or score_pct < 50.0:
                new_state = "needs_revision"
                new_conf = max(0.1, prev_conf - 0.20)
                change_reason = "Identified difficulty in concept application; targeted revision scheduled"
            else:
                # Minor stumble, keep developing
                new_conf = max(0.2, prev_conf - 0.10)
                change_reason = "Partial challenge encountered; foundational evidence preserved"

        skill_record["state"] = new_state
        skill_record["confidence"] = round(new_conf, 2)
        skill_record["attempts"] = attempts
        skill_record["last_evidence"] = {
            "type": evidence_type,
            "success": success,
            "score_pct": score_pct,
            "timestamp": now,
            "reason": change_reason
        }
        skill_record["updated_at"] = now
        states[skill_id] = skill_record
        learner_profile["skill_states"] = states
        learner_profile["updated_at"] = now

        return {
            "skill_id": skill_id,
            "previous_state": prev_state,
            "new_state": new_state,
            "confidence": round(new_conf, 2),
            "reason": change_reason
        }

    @staticmethod
    def check_prerequisites_satisfied(
        skill_id: str,
        skill_states: Dict[str, Any]
    ) -> Tuple[bool, List[str]]:
        """
        Checks whether all prerequisites for a skill are satisfied (developing or provisionally_mastered).
        Returns (is_satisfied, list_of_missing_prereqs).
        """
        skill_def = CANONICAL_SKILL_GRAPH.get(skill_id)
        if not skill_def:
            return True, []

        missing = []
        for prereq_id in skill_def.get("prerequisites", []):
            prereq_state = skill_states.get(prereq_id, {}).get("state", "unassessed")
            # Unassessed or needs_revision cannot satisfy advanced prerequisite
            if prereq_state in ["unassessed", "needs_revision"]:
                missing.append(prereq_id)

        return len(missing) == 0, missing

    @staticmethod
    def calculate_horizon_milestones(
        domain: str,
        horizon: str, # "1_month", "3_months", "6_months", "1_year", "4_years"
        weekly_hours: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Dynamically calculates high-level roadmap milestones based on chosen planning horizon and available weekly hours.
        """
        horizon_presets = {
            "1_month": {
                "name": "Intensive Accelerator Sprint (30 Days)",
                "multiplier": 0.4, # Focuses heavily on high-yield core essentials
                "granularity": "Weekly Milestones",
                "weeks": 4
            },
            "3_months": {
                "name": "Full Quarter Mastery Track (90 Days)",
                "multiplier": 0.7,
                "granularity": "Bi-weekly Sprints",
                "weeks": 12
            },
            "6_months": {
                "name": "Comprehensive Production Engineer (180 Days)",
                "multiplier": 1.0,
                "granularity": "Monthly Milestones",
                "weeks": 24
            },
            "1_year": {
                "name": "Mid-Level Professional Career Track (365 Days)",
                "multiplier": 1.5,
                "granularity": "Quarterly Phases",
                "weeks": 52
            },
            "4_years": {
                "name": "Degree-Equivalent Deep Computer Science Foundation",
                "multiplier": 3.0,
                "granularity": "Semester-Long Pillars",
                "weeks": 208
            }
        }

        preset = horizon_presets.get(horizon, horizon_presets["6_months"])
        total_study_capacity = weekly_hours * preset["weeks"]

        milestones = [
            {
                "id": "ms_foundations",
                "title": "Phase 1: Architecture & Core Languages",
                "target_hours": min(30, int(total_study_capacity * 0.25)),
                "focus_skills": ["skill_html_css", "skill_javascript_core", "skill_python_core"],
                "target_outcome": "Master fundamental syntax, control flow, and computational execution models."
            },
            {
                "id": "ms_systems",
                "title": "Phase 2: Asynchronous Systems & Frameworks",
                "target_hours": min(45, int(total_study_capacity * 0.35)),
                "focus_skills": ["skill_async_js", "skill_react_architecture", "skill_fastapi_rest"],
                "target_outcome": "Build non-blocking reactive user interfaces connected to validated RESTful APIs."
            },
            {
                "id": "ms_scale",
                "title": "Phase 3: Persistence, Infrastructure & Security",
                "target_hours": min(50, int(total_study_capacity * 0.40)),
                "focus_skills": ["skill_sql_databases", "skill_docker_containers", "skill_auth_security"],
                "target_outcome": "Deploy containerized systems with reliable database transactions and secure authentication."
            }
        ]

        if horizon in ["1_year", "4_years"]:
            milestones.append({
                "id": "ms_advanced",
                "title": "Phase 4: Distributed Systems, AI Agents & Microservices",
                "target_hours": int(total_study_capacity * 0.30),
                "focus_skills": ["skill_message_queues", "skill_rag_vector_db", "skill_kubernetes_orchestration"],
                "target_outcome": "Architect high-concurrency event-driven platforms and intelligent retrieval systems."
            })

        return milestones

    @staticmethod
    def select_next_recommended_mission(
        learner_profile: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Determines the next best 3-part mission:
        Rule 1: If any skill has 'needs_revision', assign a targeted revision mission for that foundational skill.
        Rule 2: Identify the first skill in the learner's chosen domain whose prerequisites ARE met and is not yet provisionally_mastered.
        Rule 3: Return a structured 30-minute mission: Learn (~10m GOAT video) + Practice (~15m code lab) + Prove (~5m quiz).
        """
        skill_states = learner_profile.get("skill_states", {})
        onboarding = learner_profile.get("onboarding", {})
        learning_style = onboarding.get("learning_style", "visual")
        lang_pref = onboarding.get("language_preference", "both")

        # Check Rule 1: Targeted Revision for weak skill
        for s_id, s_data in skill_states.items():
            if s_data.get("state") == "needs_revision":
                s_def = CANONICAL_SKILL_GRAPH.get(s_id, {})
                return {
                    "id": f"msn_{uuid.uuid4().hex[:8]}",
                    "skill_id": s_id,
                    "mission_type": "targeted_revision",
                    "title": f"Targeted Foundation Revision: {s_def.get('name', s_id)}",
                    "rationale": "Recent practice showed confusion in this area. Strengthening this foundation guarantees you won't struggle in advanced upcoming topics.",
                    "estimated_minutes": 25,
                    "learn_module": {
                        "topic_query": s_def.get("name", s_id),
                        "duration": "10 mins",
                        "objective": f"Review core mental models for {s_def.get('name')}"
                    },
                    "practice_module": {
                        "instructions": f"Solve the guided exercise reinforcing {s_def.get('name')}",
                        "duration": "10 mins"
                    },
                    "prove_module": {
                        "quiz_question": f"Verify fundamental understanding of {s_def.get('name')}",
                        "duration": "5 mins",
                        "xp_reward": 50
                    },
                    "status": "ready"
                }

        # Check Rule 2: Next eligible skill in roadmap sequence
        # Prioritize based on learner domain
        domain = learner_profile.get("career_goal", {}).get("primary_domain", "fullstack")
        
        # Domain preferred skill sequence
        domain_skill_order = {
            "frontend": ["skill_html_css", "skill_javascript_core", "skill_async_js", "skill_tailwind_design", "skill_react_architecture", "skill_tanstack_query", "skill_nextjs_fullstack"],
            "backend": ["skill_http_networking", "skill_python_core", "skill_fastapi_rest", "skill_sql_databases", "skill_auth_security", "skill_nosql_mongodb", "skill_redis_caching", "skill_message_queues"],
            "ai_ml": ["skill_python_core", "skill_numpy_pandas", "skill_classical_ml", "skill_pytorch_deep_learning", "skill_rag_vector_db"],
            "devops": ["skill_http_networking", "skill_docker_containers", "skill_kubernetes_orchestration"],
            "cybersecurity": ["skill_http_networking", "skill_owasp_security", "skill_auth_security"],
            "fullstack": ["skill_html_css", "skill_javascript_core", "skill_async_js", "skill_fastapi_rest", "skill_react_architecture", "skill_sql_databases", "skill_nextjs_fullstack"]
        }

        candidate_skills = domain_skill_order.get(domain, domain_skill_order["fullstack"])

        chosen_skill_id = None
        for s_id in candidate_skills:
            st = skill_states.get(s_id, {}).get("state", "unassessed")
            if st != "provisionally_mastered":
                # Check prerequisites
                satisfied, missing = PersonalizationEngine.check_prerequisites_satisfied(s_id, skill_states)
                if satisfied:
                    chosen_skill_id = s_id
                    break

        if not chosen_skill_id:
            # Fallback to first unmastered skill in graph
            for s_id in CANONICAL_SKILL_GRAPH:
                st = skill_states.get(s_id, {}).get("state", "unassessed")
                if st != "provisionally_mastered":
                    chosen_skill_id = s_id
                    break

        if not chosen_skill_id:
            chosen_skill_id = "skill_javascript_core"

        s_def = CANONICAL_SKILL_GRAPH.get(chosen_skill_id, {})
        
        return {
            "id": f"msn_{uuid.uuid4().hex[:8]}",
            "skill_id": chosen_skill_id,
            "mission_type": "progression",
            "title": f"Mastery Mission: {s_def.get('name', chosen_skill_id)}",
            "rationale": f"All prerequisites are verified. This is the optimal next milestone for your {domain.replace('_', ' ').title()} career pathway.",
            "estimated_minutes": 30,
            "learn_module": {
                "topic_query": s_def.get("name", chosen_skill_id),
                "duration": "10-12 mins",
                "objective": f"Study GOAT video masterclass on {s_def.get('name')}"
            },
            "practice_module": {
                "instructions": f"Hands-on interactive lab coding exercise for {s_def.get('name')}",
                "duration": "15 mins"
            },
            "prove_module": {
                "quiz_question": f"Complete diagnostic concept check for {s_def.get('name')}",
                "duration": "5 mins",
                "xp_reward": 50
            },
            "status": "ready"
        }
