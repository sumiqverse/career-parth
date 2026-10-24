# Complete curated roadmaps synthesizing roadmap.sh, freeCodeCamp, and Boot.dev

SEED_ROADMAPS = [
    {
        "id": "rm_fullstack",
        "slug": "full-stack-developer",
        "title": "Full Stack Web Development",
        "tagline": "From Zero to Full Stack Production Maestro",
        "description": "The complete journey from modern JavaScript and React to scalable FastAPI / Node.js backends, MongoDB / PostgreSQL databases, and cloud deployment.",
        "domain": "fullstack",
        "icon": "Layers",
        "gradient": "from-indigo-600 via-purple-600 to-pink-600",
        "difficulty": "Beginner to Advanced",
        "estimated_hours": 120,
        "total_xp": 4500,
        "source_attribution": "Synthesized from roadmap.sh (Full Stack), freeCodeCamp (Responsive Web & Full Stack), and Boot.dev (Web Dev Core)",
        "stages": [
            {
                "id": "fs_stage_1",
                "order": 1,
                "title": "Stage 1: Web Fundamentals & Modern JavaScript",
                "description": "Master the core trio of the web: semantic HTML, modern responsive CSS, and modern ES6+ JavaScript.",
                "topics": [
                    {
                        "id": "fs_topic_html_css",
                        "title": "Semantic HTML & Modern Flexbox/Grid",
                        "description": "Understand document structure, accessibility, and modern responsive layout engines.",
                        "duration_mins": 45,
                        "xp": 100,
                        "is_completed": False
                    },
                    {
                        "id": "fs_topic_js_es6",
                        "title": "Modern JavaScript (ES6+): Closures, Async/Await & APIs",
                        "description": "Deep-dive into event loops, promises, async/await, fetch API, and destructuring.",
                        "duration_mins": 60,
                        "xp": 150,
                        "is_completed": False
                    }
                ]
            },
            {
                "id": "fs_stage_2",
                "order": 2,
                "title": "Stage 2: Frontend Engineering with React & Next.js",
                "description": "Build reactive component hierarchies, manage server/client state, and render server-side.",
                "topics": [
                    {
                        "id": "fs_topic_react_core",
                        "title": "React Architecture: Hooks, State & Component Lifecycle",
                        "description": "Component composition, useState, useEffect, custom hooks, and state immutability.",
                        "duration_mins": 60,
                        "xp": 150,
                        "is_completed": False
                    },
                    {
                        "id": "fs_topic_nextjs_app_router",
                        "title": "Next.js App Router: Server Components & Data Fetching",
                        "description": "Server vs Client Components, dynamic routing, metadata SEO, and streaming UI.",
                        "duration_mins": 75,
                        "xp": 200,
                        "is_completed": False
                    }
                ]
            },
            {
                "id": "fs_stage_3",
                "order": 3,
                "title": "Stage 3: Scalable Backend & REST API Engineering",
                "description": "Design secure RESTful APIs, authenticate users, and manage server business logic.",
                "topics": [
                    {
                        "id": "fs_topic_backend_apis",
                        "title": "FastAPI & REST Architecture: Routing, Pydantic & Validation",
                        "description": "Build high-throughput async endpoints, request/response models, and status codes.",
                        "duration_mins": 60,
                        "xp": 175,
                        "is_completed": False
                    },
                    {
                        "id": "fs_topic_auth_jwt",
                        "title": "Authentication & Security: JWT, Password Hashing & RBAC",
                        "description": "Implement token-based authentication, bcrypt hashing, and protected route guards.",
                        "duration_mins": 60,
                        "xp": 175,
                        "is_completed": False
                    }
                ]
            },
            {
                "id": "fs_stage_4",
                "order": 4,
                "title": "Stage 4: Databases, Persistence & Cloud Deployment",
                "description": "Store data at scale with MongoDB and SQL, write migrations, and deploy live.",
                "topics": [
                    {
                        "id": "fs_topic_mongodb_scale",
                        "title": "MongoDB & Document Databases: Schemas, Aggregations & Indexes",
                        "description": "Master flexible NoSQL collections, BSON, compounding indexes, and pipeline queries.",
                        "duration_mins": 60,
                        "xp": 150,
                        "is_completed": False
                    },
                    {
                        "id": "fs_topic_deployment_docker",
                        "title": "Containerization & CI/CD: Docker, GitHub Actions & Vercel",
                        "description": "Package full-stack apps into multi-stage Docker containers and deploy seamlessly.",
                        "duration_mins": 60,
                        "xp": 200,
                        "is_completed": False
                    }
                ]
            }
        ]
    },
    {
        "id": "rm_backend",
        "slug": "backend-developer",
        "title": "Backend Engineering & System Architecture",
        "tagline": "Master Distributed APIs, Databases, Caching & Scalability",
        "description": "A comprehensive backend mastery path covering API design, relational & NoSQL databases, caching with Redis, message brokers, and high-concurrency systems.",
        "domain": "backend",
        "icon": "Server",
        "gradient": "from-emerald-600 via-teal-600 to-cyan-600",
        "difficulty": "Intermediate to Advanced",
        "estimated_hours": 100,
        "total_xp": 4200,
        "source_attribution": "Synthesized from roadmap.sh (Backend) and Boot.dev (Backend in Go & Python)",
        "stages": [
            {
                "id": "be_stage_1",
                "order": 1,
                "title": "Stage 1: HTTP Protocols, Network Layers & API Foundations",
                "description": "Deep understanding of TCP/IP, HTTP/1.1 vs HTTP/2/3, headers, status codes, and idempotency.",
                "topics": [
                    {
                        "id": "be_topic_http_protocols",
                        "title": "HTTP In-Depth: Headers, Caching, Methods & Sockets",
                        "description": "Master HTTP specifications, request lifecycle, TLS handshakes, and CORS headers.",
                        "duration_mins": 50,
                        "xp": 125,
                        "is_completed": False
                    },
                    {
                        "id": "be_topic_api_design",
                        "title": "RESTful API Standards & OpenAPI / Swagger Specification",
                        "description": "Design intuitive REST resources, versioning schemes, pagination, and error envelopes.",
                        "duration_mins": 55,
                        "xp": 150,
                        "is_completed": False
                    }
                ]
            },
            {
                "id": "be_stage_2",
                "order": 2,
                "title": "Stage 2: Database Mastery & Query Optimization",
                "description": "Relational schemas, ACID transactions, normalization, and NoSQL trade-offs.",
                "topics": [
                    {
                        "id": "be_topic_sql_deep",
                        "title": "PostgreSQL & Relational Modeling: Joins, Indexes & Transactions",
                        "description": "Write complex SQL queries, understand EXPLAIN ANALYZE, and prevent slow table scans.",
                        "duration_mins": 70,
                        "xp": 180,
                        "is_completed": False
                    },
                    {
                        "id": "be_topic_caching_redis",
                        "title": "Redis & In-Memory Caching Strategies",
                        "description": "Implement Cache-Aside, Write-Through, TTL strategies, and rate limiting algorithms.",
                        "duration_mins": 55,
                        "xp": 160,
                        "is_completed": False
                    }
                ]
            },
            {
                "id": "be_stage_3",
                "order": 3,
                "title": "Stage 3: Asynchronous Queues & Microservices",
                "description": "Decoupling systems with message queues, background workers, and service meshes.",
                "topics": [
                    {
                        "id": "be_topic_queues_celery",
                        "title": "Background Tasks & Message Brokers (RabbitMQ & Kafka)",
                        "description": "Decouple heavy tasks using producer-consumer queues and idempotent workers.",
                        "duration_mins": 65,
                        "xp": 190,
                        "is_completed": False
                    }
                ]
            }
        ]
    },
    {
        "id": "rm_ai_ml",
        "slug": "ai-ml-engineer",
        "title": "AI & Machine Learning Engineering",
        "tagline": "Build Intelligent Systems from Foundations to Modern LLMs",
        "description": "Master Python data science, core machine learning algorithms, deep learning with PyTorch, and modern generative AI with LangChain, RAG, and vector databases.",
        "domain": "ai_ml",
        "icon": "BrainCircuit",
        "gradient": "from-cyan-500 via-blue-600 to-indigo-700",
        "difficulty": "Intermediate to Advanced",
        "estimated_hours": 140,
        "total_xp": 5000,
        "source_attribution": "Synthesized from roadmap.sh (AI and Data Science) and freeCodeCamp (Machine Learning with Python)",
        "stages": [
            {
                "id": "ai_stage_1",
                "order": 1,
                "title": "Stage 1: Mathematics & Python for Machine Learning",
                "description": "NumPy array vectorization, Pandas data manipulation, and linear algebra fundamentals.",
                "topics": [
                    {
                        "id": "ai_topic_numpy_pandas",
                        "title": "NumPy & Pandas: Matrix Operations & Feature Engineering",
                        "description": "Master broadcasting, vectorized computation, handling missing values, and data cleaning.",
                        "duration_mins": 60,
                        "xp": 150,
                        "is_completed": False
                    },
                    {
                        "id": "ai_topic_classical_ml",
                        "title": "Classical ML: Regression, Decision Trees & Random Forests",
                        "description": "Train, evaluate, and tune supervised learning models with scikit-learn.",
                        "duration_mins": 70,
                        "xp": 180,
                        "is_completed": False
                    }
                ]
            },
            {
                "id": "ai_stage_2",
                "order": 2,
                "title": "Stage 2: Deep Learning & Neural Architectures",
                "description": "Backpropagation, PyTorch tensors, Convolutional Networks, and Transformers.",
                "topics": [
                    {
                        "id": "ai_topic_pytorch_foundations",
                        "title": "PyTorch Fundamentals: Autograd, Tensors & Training Loops",
                        "description": "Build neural networks from scratch with forward passes, loss functions, and optimizers.",
                        "duration_mins": 80,
                        "xp": 220,
                        "is_completed": False
                    }
                ]
            },
            {
                "id": "ai_stage_3",
                "order": 3,
                "title": "Stage 3: Generative AI, RAG & LLM Agents",
                "description": "Embeddings, vector databases, retrieval-augmented generation, and autonomous agent loops.",
                "topics": [
                    {
                        "id": "ai_topic_rag_embeddings",
                        "title": "Retrieval-Augmented Generation (RAG) & Vector Databases",
                        "description": "Chunk documents, generate vector embeddings, query semantic stores, and synthesize context.",
                        "duration_mins": 75,
                        "xp": 250,
                        "is_completed": False
                    }
                ]
            }
        ]
    },
    {
        "id": "rm_frontend",
        "slug": "frontend-developer",
        "title": "Frontend & UI/UX Engineering",
        "tagline": "Craft World-Class, Fluid, High-Performance Web Applications",
        "description": "Specialized path focusing on modern React, state management, animations, accessibility (a11y), Tailwind CSS, and Core Web Vitals optimization.",
        "domain": "frontend",
        "icon": "Palette",
        "gradient": "from-amber-500 via-orange-600 to-rose-600",
        "difficulty": "Beginner to Intermediate",
        "estimated_hours": 90,
        "total_xp": 3800,
        "source_attribution": "Synthesized from roadmap.sh (Frontend) and freeCodeCamp (Front End Development Libraries)",
        "stages": [
            {
                "id": "fe_stage_1",
                "order": 1,
                "title": "Stage 1: Advanced CSS, Tailwind & Design Systems",
                "description": "Tokens, CSS Grid, animations, dark mode palettes, and responsive typography.",
                "topics": [
                    {
                        "id": "fe_topic_tailwind_design_systems",
                        "title": "Tailwind CSS & Design Tokens: Building Reusable Component Libraries",
                        "description": "Design systems, atomic classes, dark mode theming, and accessible form controls.",
                        "duration_mins": 50,
                        "xp": 130,
                        "is_completed": False
                    }
                ]
            },
            {
                "id": "fe_stage_2",
                "order": 2,
                "title": "Stage 2: State Management & Client Performance",
                "description": "Zustand, React Query/TanStack, and optimizing Core Web Vitals.",
                "topics": [
                    {
                        "id": "fe_topic_tanstack_query",
                        "title": "TanStack Query & Client State: Server Cache & Optimistic Updates",
                        "description": "Master data fetching, automatic caching, deduplication, and optimistic mutations.",
                        "duration_mins": 65,
                        "xp": 170,
                        "is_completed": False
                    }
                ]
            }
        ]
    },
    {
        "id": "rm_devops",
        "slug": "devops-engineer",
        "title": "DevOps & Cloud Architecture",
        "tagline": "Automate, Orchestrate and Scale Resilient Cloud Systems",
        "description": "Master Linux systems administration, Docker containerization, Kubernetes orchestration, CI/CD with GitHub Actions, Terraform Infrastructure as Code, and cloud monitoring.",
        "domain": "devops",
        "icon": "CloudLightning",
        "gradient": "from-blue-600 via-indigo-600 to-violet-700",
        "difficulty": "Intermediate to Advanced",
        "estimated_hours": 110,
        "total_xp": 4400,
        "source_attribution": "Synthesized from roadmap.sh (DevOps) and freeCodeCamp (DevOps Bootcamp)",
        "stages": [
            {
                "id": "do_stage_1",
                "order": 1,
                "title": "Stage 1: Linux Administration & Container Foundations",
                "description": "Bash automation, networking, process management, and Docker images.",
                "topics": [
                    {
                        "id": "do_topic_docker_mastery",
                        "title": "Docker Deep Dive: Multi-Stage Builds, Volumes & Networks",
                        "description": "Write lean Dockerfiles, isolate network namespaces, and run multi-service Docker Compose.",
                        "duration_mins": 60,
                        "xp": 160,
                        "is_completed": False
                    }
                ]
            },
            {
                "id": "do_stage_2",
                "order": 2,
                "title": "Stage 2: Kubernetes & Continuous Delivery",
                "description": "Pods, Deployments, Services, Helm charts, and automated zero-downtime rollouts.",
                "topics": [
                    {
                        "id": "do_topic_kubernetes_core",
                        "title": "Kubernetes Architecture: Pods, Services, Ingress & Helm",
                        "description": "Orchestrate distributed containers, configure ingress controllers, and scale replicas.",
                        "duration_mins": 75,
                        "xp": 210,
                        "is_completed": False
                    }
                ]
            }
        ]
    },
    {
        "id": "rm_cybersecurity",
        "slug": "cyber-security",
        "title": "Cyber Security & Defensive Engineering",
        "tagline": "Defend Networks, Prevent Exploits & Conduct Penetration Testing",
        "description": "Learn network packet analysis, OWASP Top 10 web vulnerabilities, cryptography fundamentals, security auditing, and cloud security compliance.",
        "domain": "cybersecurity",
        "icon": "ShieldCheck",
        "gradient": "from-red-600 via-rose-600 to-amber-600",
        "difficulty": "Intermediate to Advanced",
        "estimated_hours": 115,
        "total_xp": 4600,
        "source_attribution": "Synthesized from roadmap.sh (Cyber Security) and freeCodeCamp (Information Security)",
        "stages": [
            {
                "id": "sec_stage_1",
                "order": 1,
                "title": "Stage 1: Web Application Security & OWASP Top 10",
                "description": "Understand how attacks happen: Injection, Broken Auth, XSS, and CSRF.",
                "topics": [
                    {
                        "id": "sec_topic_owasp_top10",
                        "title": "OWASP Top 10 Deep Dive: Exploitation & Hardening",
                        "description": "Hands-on vulnerability analysis: SQL injection, SSRF, Cross-Site Scripting, and defenses.",
                        "duration_mins": 65,
                        "xp": 175,
                        "is_completed": False
                    }
                ]
            }
        ]
    }
]

# Rich topic detail data: Lectures, Notes, Questions, Labs, Workshops
TOPIC_DETAILS = {
    "fs_topic_html_css": {
        "id": "fs_topic_html_css",
        "roadmap_slug": "full-stack-developer",
        "stage_id": "fs_stage_1",
        "title": "Semantic HTML & Modern Flexbox/Grid",
        "description": "Understand document structure, accessibility, and modern responsive layout engines.",
        "lectures": [
            {
                "id": "lec_html_1",
                "title": "HTML & CSS Complete Masterclass (freeCodeCamp Course)",
                "provider": "freeCodeCamp.org",
                "video_url": "https://www.youtube.com/embed/mU6anWqZJcc",
                "duration": "18 mins selected segment",
                "summary": "Covers semantic HTML5 tags (<header>, <main>, <nav>, <article>, <aside>, <footer>) and modern CSS layout engines (Flexbox and Grid).",
                "key_takeaways": [
                    "Semantic tags improve SEO, screen reader accessibility, and code clarity.",
                    "Flexbox is ideal for 1-dimensional layouts (rows or columns).",
                    "CSS Grid excels at 2-dimensional grid layouts with fr units and template areas.",
                    "Always design mobile-first with CSS media queries (min-width)."
                ]
            }
        ],
        "notes": """# Semantic HTML & Modern CSS Layouts

Semantic HTML gives meaning to your web structure rather than wrapping everything in generic `<div>` tags.

### 1. Essential Semantic Elements
- `<header>`: Introduces a section or page, typically holds branding and navigation.
- `<nav>`: Dedicated container for primary navigation links.
- `<main>`: Contains the unique, central content of the document.
- `<article>`: Self-contained composition that makes sense on its own (e.g. blog post, card).
- `<section>`: Thematic grouping of content, typically with a heading.
- `<footer>`: Closing metadata, copyright, links, and contact info.

### 2. Flexbox Quick Cheat Sheet
```css
.container {
  display: flex;
  justify-content: space-between; /* align items on main axis */
  align-items: center;            /* align items on cross axis */
  gap: 1.5rem;                    /* modern spacing without margin hacks */
  flex-wrap: wrap;                /* responsive flow */
}
```

### 3. CSS Grid in Action
```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}
```
Using `repeat(auto-fit, minmax(280px, 1fr))` automatically creates a fully responsive grid without a single media query!
""",
        "questions": [
            {
                "id": "q_html_1",
                "question": "Which CSS property combination creates an automatically wrapping responsive grid with no media queries?",
                "options": [
                    "grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));",
                    "display: flex; flex-direction: column; overflow: auto;",
                    "grid-columns: 3; float: left; width: 33%;",
                    "display: block; margin: 0 auto; max-width: 1200px;"
                ],
                "correct_option": 0,
                "explanation": "repeat(auto-fit, minmax(minSize, 1fr)) dynamically computes how many columns fit inside the viewport and stretches them evenly.",
                "xp": 25
            },
            {
                "id": "q_html_2",
                "question": "Why is using <main> preferred over <div id='main'>?",
                "options": [
                    "It automatically applies CSS styling in all browsers",
                    "Screen readers and assistive technologies use it as a landmark to jump directly to primary content",
                    "It improves browser JavaScript execution speed",
                    "It is required by the HTTP/2 specification"
                ],
                "correct_option": 1,
                "explanation": "Assistive technologies rely on HTML5 landmark elements like <main> and <nav> to allow keyboard users to skip repetitive navigation.",
                "xp": 25
            }
        ],
        "lab": {
            "id": "lab_html_1",
            "title": "Lab: Build a Responsive Card Container",
            "instructions": "Write a CSS rule for `.feature-grid` that uses CSS Grid with a 24px (1.5rem) gap and repeats columns using `repeat(auto-fit, minmax(250px, 1fr))`.",
            "language": "css",
            "starter_code": "/* Complete the .feature-grid rule below */\n.feature-grid {\n  display: grid;\n  /* Add gap and grid-template-columns here */\n\n}",
            "test_cases": [
                {
                    "input": "display: grid;",
                    "expected": "display: grid",
                    "description": "Grid display property is set"
                },
                {
                    "input": "minmax",
                    "expected": "minmax",
                    "description": "minmax function used for responsive columns"
                }
            ],
            "hint": "Use: grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;",
            "xp": 50
        },
        "workshop": {
            "id": "ws_html_1",
            "title": "Workshop: Responsive SaaS Landing Page Hero",
            "tagline": "Build a modern glassmorphic hero section using semantic HTML & Flexbox/Grid",
            "overview": "Synthesize what you've learned to build a live landing page hero section with badges, headline, dual CTAs, and a floating stat card.",
            "steps": [
                "Step 1: Set up the semantic <header> with logo and nav links using Flexbox justify-between.",
                "Step 2: Create the <main> container with a 2-column responsive grid layout.",
                "Step 3: Add typography with clean tracking and leading, styling gradient text with background-clip: text.",
                "Step 4: Implement interactive hover states with transform: translateY(-2px) and glowing box-shadows."
            ],
            "acceptance_criteria": [
                "Uses semantic <header>, <nav>, and <main> tags",
                "Grid collapses gracefully on screen widths below 768px",
                "Buttons have accessible focus and hover states"
            ],
            "xp": 100
        }
    },
    "fs_topic_js_es6": {
        "id": "fs_topic_js_es6",
        "roadmap_slug": "full-stack-developer",
        "stage_id": "fs_stage_1",
        "title": "Modern JavaScript (ES6+): Closures, Async/Await & APIs",
        "description": "Deep-dive into event loops, promises, async/await, fetch API, and destructuring.",
        "lectures": [
            {
                "id": "lec_js_1",
                "title": "JavaScript Async/Await & Event Loop Masterclass",
                "provider": "Boot.dev & freeCodeCamp",
                "video_url": "https://www.youtube.com/embed/8aGhZQkoFbQ",
                "duration": "24 mins",
                "summary": "Explains how the single-threaded JavaScript V8 engine handles asynchronous I/O via Call Stack, Web APIs, Microtask Queue, and Event Loop.",
                "key_takeaways": [
                    "JavaScript is single-threaded; asynchronous operations are delegated to runtime Web APIs.",
                    "Promises queue microtasks, which take precedence over macrotasks like setTimeout.",
                    "async/await is syntactic sugar over Promises that makes asynchronous code read synchronously.",
                    "Always wrap await calls in try/catch blocks for bulletproof error handling."
                ]
            }
        ],
        "notes": """# Modern JavaScript: Async/Await & The Event Loop

Understanding asynchronous JavaScript is the single most important skill for full-stack engineering.

### 1. Promises and Async/Await Pattern
```javascript
async function fetchUserRoadmap(userId) {
  try {
    const response = await fetch(`/api/users/${userId}/roadmap`);
    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Failed to load roadmap:", error.message);
    throw error;
  }
}
```

### 2. Parallel Asynchronous Operations with Promise.all
When requests do not depend on each other, fire them concurrently:
```javascript
const [roadmapRes, userProgressRes] = await Promise.all([
  fetch('/api/roadmaps/full-stack-developer'),
  fetch('/api/user/progress')
]);
```
This cuts your network wait time by up to 50%!
""",
        "questions": [
            {
                "id": "q_js_1",
                "question": "What happens if one promise rejects in Promise.all([p1, p2, p3])?",
                "options": [
                    "The remaining promises continue and return a partial array",
                    "The entire Promise.all immediately rejects with the reason of the first rejected promise",
                    "The browser retries the failed promise three times",
                    "It returns undefined for the failed promise"
                ],
                "correct_option": 1,
                "explanation": "Promise.all has fail-fast behavior: if any passed promise rejects, Promise.all immediately rejects with that error. (Use Promise.allSettled if you need results of all promises regardless of rejections).",
                "xp": 25
            }
        ],
        "lab": {
            "id": "lab_js_1",
            "title": "Lab: Asynchronous Data Aggregator Function",
            "instructions": "Implement an async function `loadUserTrack(apiUrl)` that fetches JSON from `apiUrl`, extracts the `track` property, and returns it.",
            "language": "javascript",
            "starter_code": "async function loadUserTrack(apiUrl) {\n  // Fetch data from apiUrl and return data.track\n  \n}",
            "test_cases": [
                {
                    "input": "apiUrl",
                    "expected": "track",
                    "description": "Extracts track property from parsed JSON"
                }
            ],
            "hint": "const res = await fetch(apiUrl); const data = await res.json(); return data.track;",
            "xp": 50
        },
        "workshop": {
            "id": "ws_js_1",
            "title": "Workshop: Real-time Currency / Crypto Rate Tracker",
            "tagline": "Build an async rate fetcher with exponential backoff and error recovery",
            "overview": "Implement a resilient async data pipeline that polls public exchange APIs, caches results in localStorage, and handles network offline events gracefully.",
            "steps": [
                "Step 1: Set up async fetch wrapper with timeout support via AbortController.",
                "Step 2: Add retry logic with exponential backoff.",
                "Step 3: Update UI state reactively with the fetched rates."
            ],
            "acceptance_criteria": [
                "Uses async/await with try/catch",
                "Uses AbortController for request cancellation",
                "Displays user-friendly errors on network failure"
            ],
            "xp": 100
        }
    },
    "fs_topic_backend_apis": {
        "id": "fs_topic_backend_apis",
        "roadmap_slug": "full-stack-developer",
        "stage_id": "fs_stage_3",
        "title": "FastAPI & REST Architecture: Routing, Pydantic & Validation",
        "description": "Build high-throughput async endpoints, request/response models, and status codes.",
        "lectures": [
            {
                "id": "lec_fastapi_1",
                "title": "FastAPI Full Course for Beginners",
                "provider": "freeCodeCamp.org",
                "video_url": "https://www.youtube.com/embed/7t2alSnE2-I",
                "duration": "30 mins selected",
                "summary": "Learn modern Python backend development using FastAPI, automatic OpenAPI Swagger docs, Pydantic type validation, and dependency injection.",
                "key_takeaways": [
                    "FastAPI is built on Starlette and Pydantic, making it one of the fastest Python frameworks.",
                    "Type annotations provide automatic data validation and interactive documentation at /docs.",
                    "Use async def for endpoints performing I/O bound tasks like database queries.",
                    "Status codes communicate intent: 200 (OK), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found)."
                ]
            }
        ],
        "notes": """# Building Scalable APIs with FastAPI

FastAPI combines pythonic type hints with blazing speed and automatic validation.

### 1. Minimal FastAPI Route with Pydantic
```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Horizon Learning API")

class RoadmapCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    domain: str
    estimated_hours: int = Field(gt=0)

@app.post("/api/roadmaps", status_code=status.HTTP_201_CREATED)
async def create_roadmap(payload: RoadmapCreate):
    # Payload is guaranteed to be validated against schema
    new_roadmap = payload.model_dump()
    return {"status": "success", "data": new_roadmap}
```
""",
        "questions": [
            {
                "id": "q_fastapi_1",
                "question": "What happens when a client sends invalid JSON types to a FastAPI endpoint using Pydantic?",
                "options": [
                    "FastAPI automatically returns a 422 Unprocessable Entity with detailed field error explanations",
                    "The server throws an unhandled 500 Internal Server Error",
                    "FastAPI silently coerces all invalid fields to None",
                    "The request hangs indefinitely"
                ],
                "correct_option": 0,
                "explanation": "Pydantic catches type mismatches before your route function runs and returns a structured 422 response detailing exactly which fields failed validation.",
                "xp": 25
            }
        ],
        "lab": {
            "id": "lab_fastapi_1",
            "title": "Lab: Create a Validated User Registration Schema",
            "instructions": "Define a Pydantic model `UserRegister` with `email: str`, `password: str`, and `full_name: str`.",
            "language": "python",
            "starter_code": "from pydantic import BaseModel\n\n# Create UserRegister model here\nclass UserRegister(BaseModel):\n    pass\n",
            "test_cases": [
                {
                    "input": "email",
                    "expected": "email",
                    "description": "email field exists"
                },
                {
                    "input": "password",
                    "expected": "password",
                    "description": "password field exists"
                }
            ],
            "hint": "class UserRegister(BaseModel):\n    email: str\n    password: str\n    full_name: str",
            "xp": 50
        },
        "workshop": {
            "id": "ws_fastapi_1",
            "title": "Workshop: Build a Complete RESTful Roadmap Microservice",
            "tagline": "CRUD endpoints with MongoDB persistence and automatic OpenAPI docs",
            "overview": "Implement GET, POST, PUT, and DELETE endpoints with query filtering, pagination, and error handling.",
            "steps": [
                "Step 1: Set up FastAPI router with tags.",
                "Step 2: Connect async MongoDB collection.",
                "Step 3: Implement pagination using limit and skip query params.",
                "Step 4: Verify generated OpenAPI docs at /docs."
            ],
            "acceptance_criteria": [
                "Includes all 4 HTTP methods",
                "Validates payloads with Pydantic",
                "Proper status codes returned"
            ],
            "xp": 100
        }
    }
}
