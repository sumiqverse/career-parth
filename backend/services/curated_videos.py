"""
Curated GOAT (Greatest Of All Time) YouTube Educational Video Service.
Provides verified, legendary educational videos from top creators (Global Legends + Hinglish GOATs)
with personalized recommendation matching, multi-option switcher, ratings, and takeaway notes.
"""

from typing import Dict, Any, List, Optional

# Verified GOAT video repository mapped by keywords and canonical topic identifiers
CURATED_GOAT_CATALOG: Dict[str, List[Dict[str, Any]]] = {
    # 1. HTML & CSS / Layouts
    "html_css": [
        {
            "id": "vid_kevin_css_grid",
            "title": "Learn CSS Grid & Modern Layouts the Easy Way",
            "provider": "Kevin Powell (CSS King)",
            "video_url": "https://www.youtube.com/embed/1Rs2ND1ryYc",
            "duration": "24 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.98,
            "view_count": "1.8M+ views",
            "level": "beginner",
            "summary": "Kevin Powell breaks down CSS Grid, minmax(), fr units, and fluid responsive layouts without complex media queries.",
            "key_takeaways": [
                "Use repeat(auto-fit, minmax(280px, 1fr)) for automatic responsive wrapping",
                "CSS Grid provides 2D layout control while Flexbox is 1D",
                "Gap property replaces fragile margin hacks",
                "Mobile-first design principles ensure optimal rendering on every device"
            ]
        },
        {
            "id": "vid_fcc_html_full",
            "title": "HTML & CSS Full Course - Beginner to Pro",
            "provider": "freeCodeCamp.org & SuperSimpleDev",
            "video_url": "https://www.youtube.com/embed/G3e-cpL7ofc",
            "duration": "6 hours comprehensive",
            "style": "comprehensive_masterclass",
            "creator_type": "global_goat",
            "rating": 4.95,
            "view_count": "12M+ views",
            "level": "beginner",
            "summary": "Complete zero-to-hero HTML & CSS masterclass covering all semantic elements, forms, accessibility, and modern positioning.",
            "key_takeaways": [
                "Semantic tags (<header>, <nav>, <main>, <article>, <footer>) maximize SEO and a11y",
                "Box model fundamentals: content, padding, border, margin",
                "CSS specificity rules and cascading hierarchy",
                "Responsive design with flexbox and media queries"
            ]
        },
        {
            "id": "vid_chai_html_css",
            "title": "HTML & CSS Complete Masterclass in Hindi",
            "provider": "Chai aur Code (Hitesh Choudhary)",
            "video_url": "https://www.youtube.com/embed/HD13eq_Pmp8",
            "duration": "35 mins",
            "style": "hinglish_regional",
            "creator_type": "hinglish_goat",
            "rating": 4.97,
            "view_count": "850K+ views",
            "level": "beginner",
            "summary": "Hitesh Choudhary explains semantic HTML structure and CSS layouts with real production mental models in crystal-clear Hinglish.",
            "key_takeaways": [
                "Real-world DOM tree visualization and browser parsing",
                "Flex container vs flex items alignment properties",
                "Clean CSS class naming and modular organization",
                "Building real responsive components without bloat"
            ]
        }
    ],

    # 2. Modern JavaScript / Event Loop / Async
    "javascript": [
        {
            "id": "vid_philip_event_loop",
            "title": "What the heck is the event loop anyway? | JSConf EU",
            "provider": "Philip Roberts (JSConf EU)",
            "video_url": "https://www.youtube.com/embed/8aGhZQkoFbQ",
            "duration": "26 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.99,
            "view_count": "3.5M+ views",
            "level": "intermediate",
            "summary": "The undisputed greatest JavaScript video of all time. Visualizes how the single-threaded V8 engine handles asynchronous I/O.",
            "key_takeaways": [
                "JavaScript runtime has one call stack and executes one frame at a time",
                "Async operations (fetch, setTimeout, DOM events) are handed off to Web APIs",
                "The Event Loop checks if Call Stack is empty before dequeuing Microtasks and Macrotasks",
                "Never block the call stack with heavy CPU synchronous loops"
            ]
        },
        {
            "id": "vid_akshay_namaste_js",
            "title": "Namaste JavaScript: Closures & Execution Context",
            "provider": "Akshay Saini (Namaste JS)",
            "video_url": "https://www.youtube.com/embed/pN6jk0uUrD8",
            "duration": "21 mins",
            "style": "hinglish_regional",
            "creator_type": "hinglish_goat",
            "rating": 4.98,
            "view_count": "2.1M+ views",
            "level": "intermediate",
            "summary": "India's highest rated JavaScript series explaining Call Stack, Memory Creation Phase, Scope Chain, and Lexical Environment.",
            "key_takeaways": [
                "Execution context contains Memory Component (Variable Environment) and Code Component (Thread of Execution)",
                "Hoisting occurs because memory is allocated to variables and functions before code runs",
                "Closures retain access to their lexical scope even when invoked outside it",
                "Data hiding and encapsulation through factory functions"
            ]
        },
        {
            "id": "vid_fireship_async_js",
            "title": "The Async Await Episode I Promised",
            "provider": "Fireship",
            "video_url": "https://www.youtube.com/embed/vn3tm0quoqE",
            "duration": "10 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.96,
            "view_count": "2.4M+ views",
            "level": "beginner",
            "summary": "High-octane visual breakdown comparing callbacks, Promises, and modern async/await patterns with error handling best practices.",
            "key_takeaways": [
                "Async functions always wrap their return value in a Promise",
                "Await pauses function execution without blocking the main browser thread",
                "Promise.all allows parallel I/O dispatch; Promise.allSettled avoids fail-fast rejections",
                "Always wrap await in try/catch or use high-order promise error handlers"
            ]
        }
    ],

    # 3. React Architecture
    "react": [
        {
            "id": "vid_dan_react_arch",
            "title": "React Architecture, Server Components & Hooks in Depth",
            "provider": "Jack Herrington & Dan Abramov",
            "video_url": "https://www.youtube.com/embed/w7ejDZ8SWv8",
            "duration": "28 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.97,
            "view_count": "900K+ views",
            "level": "intermediate",
            "summary": "In-depth breakdown of React's reconciliation engine, Fiber architecture, state batching, and custom hook patterns.",
            "key_takeaways": [
                "Components are pure functions that project state onto immutable virtual DOM trees",
                "Hooks must follow the rule of hooks: always call at top level, never conditionally",
                "State updates in React 18+ are batched automatically across all event handlers",
                "Lift state up only to the lowest common ancestor to minimize re-renders"
            ]
        },
        {
            "id": "vid_chai_react_hindi",
            "title": "Chai aur React: Complete Series for Beginners & Pros",
            "provider": "Chai aur Code (Hitesh Choudhary)",
            "video_url": "https://www.youtube.com/embed/vz1RlUyrc3w",
            "duration": "42 mins",
            "style": "hinglish_regional",
            "creator_type": "hinglish_goat",
            "rating": 4.98,
            "view_count": "1.5M+ views",
            "level": "beginner",
            "summary": "Comprehensive hands-on breakdown of React from scratch: JSX transpilation, hooks, props drilling vs Context API, and state immutability.",
            "key_takeaways": [
                "React creates a Virtual DOM tree to calculate minimal diff mutations",
                "useState triggers a re-render; never mutate state directly",
                "useEffect cleanups prevent memory leaks and dangling subscriptions",
                "Building reusable custom hooks for API calls and form validation"
            ]
        },
        {
            "id": "vid_fireship_react_100s",
            "title": "React in 100 Seconds + Full Tour",
            "provider": "Fireship",
            "video_url": "https://www.youtube.com/embed/Tn6-PIqc4UM",
            "duration": "12 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.94,
            "view_count": "2.8M+ views",
            "level": "beginner",
            "summary": "Rapid-fire visual walkthrough of components, JSX, props, state, effect hooks, and React 19 features.",
            "key_takeaways": [
                "JSX is syntactic sugar for React.createElement()",
                "Props pass data down, callbacks pass events up",
                "React is unopinionated; combine with modern tools like Vite and Next.js"
            ]
        }
    ],

    # 4. Next.js App Router
    "nextjs": [
        {
            "id": "vid_lee_nextjs_router",
            "title": "Next.js App Router: Complete Architecture Deep Dive",
            "provider": "Lee Robinson (VP of Product, Vercel)",
            "video_url": "https://www.youtube.com/embed/gSSsZReIFRk",
            "duration": "32 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.97,
            "view_count": "1.1M+ views",
            "level": "intermediate",
            "summary": "The official masterclass by Vercel's product head on Server Components, Client Components, dynamic routes, streaming Suspense, and metadata.",
            "key_takeaways": [
                "React Server Components execute only on the server, sending zero JS bundle to the client",
                "'use client' boundary declares interactive client components",
                "Streaming with React Suspense unlocks instant perceived loading speeds",
                "Server actions provide type-safe mutations without manual REST boilerplate"
            ]
        },
        {
            "id": "vid_chai_nextjs_hindi",
            "title": "Next.js Complete Course in Hindi (App Router & SSR)",
            "provider": "Chai aur Code (Hitesh Choudhary)",
            "video_url": "https://www.youtube.com/embed/41fP43p4p9k",
            "duration": "45 mins",
            "style": "hinglish_regional",
            "creator_type": "hinglish_goat",
            "rating": 4.96,
            "view_count": "720K+ views",
            "level": "beginner",
            "summary": "Hitesh explains App Router conventions, layout nesting, route handlers, database connections, and Vercel cloud deployment.",
            "key_takeaways": [
                "File-based routing with page.tsx, layout.tsx, and loading.tsx",
                "Caching tiers in Next.js: Request memoization, Data Cache, Full Route Cache",
                "Connecting MongoDB and Prisma safely without connection leaks",
                "Environment variable security and NextAuth / JWT setup"
            ]
        }
    ],

    # 5. FastAPI & Python Backend Architecture
    "fastapi": [
        {
            "id": "vid_sanjeev_fastapi_full",
            "title": "Python FastAPI Full Course - Comprehensive REST APIs",
            "provider": "Sanjeev Thiyagarajan & freeCodeCamp",
            "video_url": "https://www.youtube.com/embed/0sOvCWFmrtA",
            "duration": "19 hours complete (Selected Core Segment)",
            "style": "comprehensive_masterclass",
            "creator_type": "global_goat",
            "rating": 4.98,
            "view_count": "1.7M+ views",
            "level": "intermediate",
            "summary": "The definitive production FastAPI masterclass covering Starlette, Pydantic, SQLAlchemy/Motor, JWT auth, and Docker deployment.",
            "key_takeaways": [
                "FastAPI leverages Python type hints for automatic Swagger/OpenAPI documentation",
                "Async def endpoints provide asynchronous non-blocking event loop execution",
                "Pydantic schemas enforce strict runtime validation on requests and responses",
                "Dependency injection system (Depends) simplifies auth and database sessions"
            ]
        },
        {
            "id": "vid_amigoscode_fastapi",
            "title": "FastAPI Crash Course: Build Modern High-Speed APIs",
            "provider": "Amigoscode",
            "video_url": "https://www.youtube.com/embed/7t2alSnE2-I",
            "duration": "35 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.94,
            "view_count": "650K+ views",
            "level": "beginner",
            "summary": "Clean, focused tutorial on setting up routing, models, path & query parameters, and testing via interactive docs.",
            "key_takeaways": [
                "Automatic 422 validation errors with exact failure details",
                "Status codes: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found",
                "Uvicorn ASGI server deployment configuration"
            ]
        }
    ],

    # 6. Authentication & Security (JWT, bcrypt, OAuth)
    "auth": [
        {
            "id": "vid_wds_jwt",
            "title": "JWT Authentication Tutorial - What is JWT and How Does It Work?",
            "provider": "Web Dev Simplified",
            "video_url": "https://www.youtube.com/embed/mbsmsi7l3r4",
            "duration": "18 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.95,
            "view_count": "2.1M+ views",
            "level": "intermediate",
            "summary": "Kyle breaks down JSON Web Tokens into Header, Payload, and Signature, explaining symmetric vs asymmetric signing and access/refresh token rotation.",
            "key_takeaways": [
                "JWTs are stateless; the signature verifies payload integrity without database lookups",
                "Never store confidential secrets (passwords, social security numbers) inside the unencrypted payload",
                "Short-lived Access Tokens (15m) + long-lived HttpOnly Refresh Tokens (7d)",
                "Bcrypt salted hashing protects passwords against rainbow table attacks"
            ]
        },
        {
            "id": "vid_bytebytego_oauth_jwt",
            "title": "OAuth 2.0 and OpenID Connect Explained in 10 Minutes",
            "provider": "ByteByteGo",
            "video_url": "https://www.youtube.com/embed/996OiexHze0",
            "duration": "11 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.97,
            "view_count": "1.6M+ views",
            "level": "intermediate",
            "summary": "Visual architectural diagrams illustrating authorization code flow with PKCE, token exchanges, and token validation.",
            "key_takeaways": [
                "Authentication (Who you are) vs Authorization (What you can access)",
                "Authorization Code flow prevents leaking access tokens in browser history",
                "Role-Based Access Control (RBAC) verifies permissions per endpoint"
            ]
        },
        {
            "id": "vid_chai_auth_hindi",
            "title": "Authentication & JWT Architecture in Hindi",
            "provider": "Chai aur Code (Hitesh Choudhary)",
            "video_url": "https://www.youtube.com/embed/Z57566JBa84",
            "duration": "38 mins",
            "style": "hinglish_regional",
            "creator_type": "hinglish_goat",
            "rating": 4.96,
            "view_count": "540K+ views",
            "level": "beginner",
            "summary": "Deep dive into cookies vs localStorage, CSRF protection, HttpOnly cookies, and token verification middlewares in Hindi.",
            "key_takeaways": [
                "Never store access tokens in localStorage due to XSS vulnerability",
                "HttpOnly and SameSite cookie attributes block client-side JavaScript theft",
                "Middleware authorization checks verify decoded token sub and roles",
                "Handling token expiration gracefully on the frontend"
            ]
        }
    ],

    # 7. MongoDB & NoSQL Scale
    "mongodb": [
        {
            "id": "vid_traversy_mongo",
            "title": "MongoDB Crash Course - Collections, Queries & Aggregation",
            "provider": "Traversy Media",
            "video_url": "https://www.youtube.com/embed/ofme2o29ngU",
            "duration": "30 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.93,
            "view_count": "1.9M+ views",
            "level": "beginner",
            "summary": "Brad Traversy provides a clear hands-on tutorial on MongoDB CRUD operations, operators ($set, $inc, $push), and Compass GUI.",
            "key_takeaways": [
                "MongoDB stores data as flexible, schema-less BSON documents inside collections",
                "Atomic updates using operators ($set, $inc, $pull) eliminate race conditions",
                "Document embedding vs document referencing design trade-offs",
                "Compound indexes speed up multi-field queries exponentially"
            ]
        },
        {
            "id": "vid_hussein_mongo_index",
            "title": "Database Indexing & MongoDB Performance Engineering",
            "provider": "Hussein Nasser (Software Engineering Expert)",
            "video_url": "https://www.youtube.com/embed/aytw0bE2qkg",
            "duration": "28 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.98,
            "view_count": "620K+ views",
            "level": "advanced",
            "summary": "Hussein explains B-Tree indexing, index scans vs table scans, write amplification, and aggregation pipelines at scale.",
            "key_takeaways": [
                "Indexes allow O(log N) lookup; unindexed fields trigger full collection scans (COLLSCAN)",
                "The ESR rule (Equality, Sort, Range) dictates optimal index field ordering",
                "Aggregation pipeline stages ($match, $group, $project) run in memory on the cluster"
            ]
        }
    ],

    # 8. Docker & Containerization
    "docker": [
        {
            "id": "vid_nana_docker_full",
            "title": "Docker Tutorial for Beginners [Full Course]",
            "provider": "TechWorld with Nana",
            "video_url": "https://www.youtube.com/embed/3c-iBn73dDE",
            "duration": "2.5 hours complete (Selected Core)",
            "style": "comprehensive_masterclass",
            "creator_type": "global_goat",
            "rating": 4.99,
            "view_count": "7.5M+ views",
            "level": "beginner",
            "summary": "The highest-rated DevOps video on YouTube. Nana explains images, containers, networks, volumes, and Dockerfile optimization.",
            "key_takeaways": [
                "A container is an isolated Linux process running on shared host OS kernel",
                "Images are built in read-only cached layers; order instructions from least to most frequent changes",
                "Multi-stage Docker builds separate build tools from lean production runtime",
                "Docker Compose coordinates multi-container stacks (Frontend + Backend + Database)"
            ]
        },
        {
            "id": "vid_fireship_docker_100s",
            "title": "Docker in 100 Seconds + Practical Walkthrough",
            "provider": "Fireship",
            "video_url": "https://www.youtube.com/embed/Gjnup-PuquQ",
            "duration": "12 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.95,
            "view_count": "3.1M+ views",
            "level": "beginner",
            "summary": "Speedrun through container virtualization, cgroups, namespaces, and Docker CLI commands.",
            "key_takeaways": [
                "Solves the 'it works on my machine' paradox by packaging code and environment together",
                "Docker hub image registry and tag versioning",
                "Volume mounts enable live hot-reload in local development"
            ]
        },
        {
            "id": "vid_babbar_docker_hindi",
            "title": "Docker & Containerization Complete Guide in Hindi",
            "provider": "Love Babbar (CodeHelp)",
            "video_url": "https://www.youtube.com/embed/rOTqprHv1YE",
            "duration": "45 mins",
            "style": "hinglish_regional",
            "creator_type": "hinglish_goat",
            "rating": 4.97,
            "view_count": "980K+ views",
            "level": "beginner",
            "summary": "Babbar explains containers vs virtual machines, Docker daemon architecture, port mapping, and production container tips in Hindi.",
            "key_takeaways": [
                "VM hypervisor overhead vs container kernel isolation",
                "Port mapping syntax: host_port:container_port",
                "Docker network drivers: bridge, host, overlay",
                "Writing clean Dockerfiles for Node and Python web apps"
            ]
        }
    ],

    # 9. Kubernetes & Cloud Orchestration
    "kubernetes": [
        {
            "id": "vid_nana_k8s_master",
            "title": "Kubernetes Tutorial for Beginners [Complete Masterclass]",
            "provider": "TechWorld with Nana",
            "video_url": "https://www.youtube.com/embed/X48VuDVv0do",
            "duration": "3.5 hours complete",
            "style": "comprehensive_masterclass",
            "creator_type": "global_goat",
            "rating": 4.99,
            "view_count": "5.8M+ views",
            "level": "intermediate",
            "summary": "The gold standard Kubernetes course covering Pods, Deployments, Services, ConfigMaps, Ingress Controllers, and kubectl command mastery.",
            "key_takeaways": [
                "Master node components: API Server, Scheduler, Controller Manager, etcd key-value store",
                "Worker node components: kubelet, kube-proxy, container runtime",
                "Deployments manage ReplicaSets for declarative rolling zero-downtime updates",
                "Services provide stable internal DNS and load balancing across dynamic ephemeral pods"
            ]
        },
        {
            "id": "vid_fireship_k8s_100s",
            "title": "Kubernetes in 100 Seconds",
            "provider": "Fireship",
            "video_url": "https://www.youtube.com/embed/PivpCKEiQOQ",
            "duration": "9 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.94,
            "view_count": "1.9M+ views",
            "level": "beginner",
            "summary": "Rapid overview of container orchestration, self-healing clusters, and auto-scaling.",
            "key_takeaways": [
                "Automates horizontal pod autoscaling (HPA) based on CPU/memory load",
                "Self-healing: restarts failed containers and reschedules pods when nodes die",
                "Helm charts act as the package manager for Kubernetes"
            ]
        }
    ],

    # 10. HTTP Protocols & Network Architecture
    "http_networking": [
        {
            "id": "vid_hussein_http3",
            "title": "HTTP/1.1 vs HTTP/2 vs HTTP/3 (QUIC) Deep Dive",
            "provider": "Hussein Nasser",
            "video_url": "https://www.youtube.com/embed/a-sBfyiXysI",
            "duration": "28 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.98,
            "view_count": "890K+ views",
            "level": "intermediate",
            "summary": "Comprehensive network engineering masterclass exploring TCP head-of-line blocking, TLS handshakes, binary framing, and UDP-based QUIC.",
            "key_takeaways": [
                "HTTP/1.1 suffers from Head-of-Line (HoL) blocking on single TCP streams",
                "HTTP/2 introduces binary framing and multiplexed streams over a single TCP connection",
                "HTTP/3 replaces TCP with UDP-based QUIC, eliminating transport-level HoL blocking",
                "Idempotency: GET, PUT, DELETE are idempotent; POST is non-idempotent"
            ]
        },
        {
            "id": "vid_bytebytego_internet",
            "title": "How the Internet Really Works: DNS, TCP, and TLS",
            "provider": "ByteByteGo",
            "video_url": "https://www.youtube.com/embed/7_LPdttKXPc",
            "duration": "12 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.97,
            "view_count": "2.1M+ views",
            "level": "beginner",
            "summary": "Visual architectural breakdown of recursive DNS lookups, TCP 3-way handshakes, and TLS certificate validation.",
            "key_takeaways": [
                "DNS translates human domain names into IP addresses through Root, TLD, and Authoritative servers",
                "TCP 3-way handshake: SYN, SYN-ACK, ACK guarantees ordered delivery",
                "TLS asymmetric key exchange secures symmetric AES payload encryption"
            ]
        }
    ],

    # 11. SQL & Relational Database Engineering
    "sql_postgres": [
        {
            "id": "vid_alex_sql_full",
            "title": "SQL Full Course for Beginners to Advanced",
            "provider": "Alex The Analyst",
            "video_url": "https://www.youtube.com/embed/HXV3zeRR3h4",
            "duration": "4 hours complete",
            "style": "comprehensive_masterclass",
            "creator_type": "global_goat",
            "rating": 4.98,
            "view_count": "3.8M+ views",
            "level": "beginner",
            "summary": "Top-ranked SQL masterclass covering SELECT, GROUP BY, INNER/LEFT/RIGHT/FULL JOINs, Window Functions, and Subqueries.",
            "key_takeaways": [
                "Relational schema normalization (1NF, 2NF, 3NF) eliminates data redundancy",
                "JOIN mechanics: INNER JOIN matches both tables; LEFT JOIN keeps all left rows",
                "Window functions (ROW_NUMBER, RANK, OVER) calculate aggregations without collapsing rows",
                "ACID properties (Atomicity, Consistency, Isolation, Durability) guarantee transactional reliability"
            ]
        },
        {
            "id": "vid_hussein_db_index",
            "title": "Database Indexes - What You Need to Know",
            "provider": "Hussein Nasser",
            "video_url": "https://www.youtube.com/embed/HubezKbFL7E",
            "duration": "22 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.97,
            "view_count": "1.2M+ views",
            "level": "intermediate",
            "summary": "EXPLAIN ANALYZE deep dive showing sequential scans vs index scans, B-Trees, and clustered vs secondary indexes in PostgreSQL.",
            "key_takeaways": [
                "Indexes create sorted B-Tree pointers to disk table pages",
                "Over-indexing degrades write (INSERT, UPDATE) performance",
                "Use EXPLAIN ANALYZE to detect slow sequential scans and query bottlenecks"
            ]
        },
        {
            "id": "vid_chai_sql_hindi",
            "title": "SQL & PostgreSQL Complete Tutorial in Hindi",
            "provider": "Chai aur Code (Hitesh Choudhary)",
            "video_url": "https://www.youtube.com/embed/hlGoQC332VM",
            "duration": "40 mins",
            "style": "hinglish_regional",
            "creator_type": "hinglish_goat",
            "rating": 4.96,
            "view_count": "610K+ views",
            "level": "beginner",
            "summary": "Clear, practical guide to relational databases, schema design, foreign keys, migrations, and connecting with backend ORMs.",
            "key_takeaways": [
                "Primary Key and Foreign Key constraints preserve referential integrity",
                "Writing parameterized queries prevents catastrophic SQL Injection attacks",
                "Database transactions with BEGIN, COMMIT, and ROLLBACK",
                "Connecting PostgreSQL with Node.js and Python safely"
            ]
        }
    ],

    # 12. Redis & In-Memory Caching
    "redis_caching": [
        {
            "id": "vid_bytebytego_redis",
            "title": "Top Redis Use Cases & Caching Architecture",
            "provider": "ByteByteGo",
            "video_url": "https://www.youtube.com/embed/jgpVdJB2yKQ",
            "duration": "14 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.97,
            "view_count": "1.4M+ views",
            "level": "intermediate",
            "summary": "Architectural guide explaining Cache-Aside, Write-Through, Write-Back, TTL eviction policies, and Redis Distributed Locking.",
            "key_takeaways": [
                "Cache-Aside pattern: Application checks cache; on miss, loads from DB and writes to cache",
                "In-memory sub-millisecond latency prevents relational database CPU exhaustion",
                "Eviction policies: LRU (Least Recently Used) and LFU (Least Frequently Used)",
                "Implementing token bucket rate-limiting algorithms with Redis INCR and EXPIRE"
            ]
        },
        {
            "id": "vid_fireship_redis_100s",
            "title": "Redis in 100 Seconds",
            "provider": "Fireship",
            "video_url": "https://www.youtube.com/embed/G1rOthIU-uo",
            "duration": "8 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.95,
            "view_count": "1.7M+ views",
            "level": "beginner",
            "summary": "Fast-paced breakdown of Redis data structures: Strings, Hashes, Lists, Sets, Sorted Sets, and Pub/Sub messaging.",
            "key_takeaways": [
                "Single-threaded event loop ensures atomic operations without locking overhead",
                "Persistence options: RDB snapshots and AOF (Append Only File) logs",
                "Pub/Sub enables lightweight real-time notifications"
            ]
        }
    ],

    # 13. Background Queues & Message Brokers (Kafka / RabbitMQ / Celery)
    "queues_kafka": [
        {
            "id": "vid_hussein_kafka_rabbit",
            "title": "Kafka vs RabbitMQ - Architectural Tradeoffs",
            "provider": "Hussein Nasser",
            "video_url": "https://www.youtube.com/embed/o0k8x2rQe5Y",
            "duration": "27 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.98,
            "view_count": "750K+ views",
            "level": "advanced",
            "summary": "Compares smart broker/dumb consumer (RabbitMQ) vs dumb broker/smart consumer distributed commit log (Kafka).",
            "key_takeaways": [
                "RabbitMQ routes discrete messages via exchanges; removes messages after acknowledgment",
                "Kafka persists streaming events in append-only partitions with consumer group offset tracking",
                "Decouples slow I/O (video rendering, email dispatch) from user-facing API request cycles",
                "Idempotent message processing prevents duplicate side-effects during network retries"
            ]
        },
        {
            "id": "vid_bytebytego_message_queue",
            "title": "What is a Message Queue and Why Use It?",
            "provider": "ByteByteGo",
            "video_url": "https://www.youtube.com/embed/fmj0u0g3b_M",
            "duration": "10 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.96,
            "view_count": "1.2M+ views",
            "level": "intermediate",
            "summary": "Visual overview of asynchronous decoupling, traffic smoothing (peak shaving), and fault tolerance.",
            "key_takeaways": [
                "Asynchronous producer-consumer decoupling prevents cascading service outages",
                "Dead-letter queues (DLQ) capture malformed payloads for debugging",
                "Worker pooling enables seamless horizontal background scaling"
            ]
        }
    ],

    # 14. NumPy, Pandas & Data Engineering
    "data_science_python": [
        {
            "id": "vid_keith_pandas_full",
            "title": "Solving Real-World Data Science Tasks with Python Pandas",
            "provider": "Keith Galli",
            "video_url": "https://www.youtube.com/embed/vmEHCJofslg",
            "duration": "55 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.98,
            "view_count": "2.4M+ views",
            "level": "beginner",
            "summary": "Legendary hands-on real-world data science project analyzing 12 months of sales data with Pandas.",
            "key_takeaways": [
                "Vectorized array operations outperform slow Python for-loops by up to 100x",
                "Data cleaning: handling NaN, type casting with pd.to_numeric, and datetime parsing",
                "Aggregations: groupby(), agg(), and filtering with boolean indexing",
                "Exporting analytical insights and visualizations cleanly"
            ]
        },
        {
            "id": "vid_fcc_numpy_master",
            "title": "Python NumPy Complete Tutorial for Beginners",
            "provider": "freeCodeCamp.org & Keith Galli",
            "video_url": "https://www.youtube.com/embed/QUT1VHiLmmI",
            "duration": "58 mins",
            "style": "comprehensive_masterclass",
            "creator_type": "global_goat",
            "rating": 4.96,
            "view_count": "1.8M+ views",
            "level": "beginner",
            "summary": "In-depth guide to multidimensional arrays, indexing, slicing, broadcasting arithmetic, and linear algebra math.",
            "key_takeaways": [
                "NumPy ndarray stores homogeneous memory buffers in contiguous C arrays",
                "Broadcasting rules allow arithmetic between arrays of different compatible shapes",
                "Matrix multiplication (np.dot, @) and statistical functions (mean, std, var)",
                "Memory efficiency vs standard Python nested lists"
            ]
        },
        {
            "id": "vid_harry_ds_hindi",
            "title": "NumPy & Pandas Complete Data Analysis in Hindi",
            "provider": "CodeWithHarry",
            "video_url": "https://www.youtube.com/embed/r-uOLxNrNk8",
            "duration": "48 mins",
            "style": "hinglish_regional",
            "creator_type": "hinglish_goat",
            "rating": 4.95,
            "view_count": "1.6M+ views",
            "level": "beginner",
            "summary": "Harry explains data structures (Series, DataFrame), indexing (loc vs iloc), and data manipulation in Hindi.",
            "key_takeaways": [
                "DataFrame indexing with loc (label-based) and iloc (integer position-based)",
                "Dropping and imputing missing data values",
                "Merging, joining, and concatenating multiple data sources",
                "Visualizing trends with Matplotlib and Seaborn"
            ]
        }
    ],

    # 15. Classical Machine Learning & Scikit-Learn
    "classical_ml": [
        {
            "id": "vid_statquest_ml",
            "title": "Machine Learning Fundamentals: Trees, Regressions & Forests",
            "provider": "StatQuest with Josh Starmer",
            "video_url": "https://www.youtube.com/embed/Gv9_4yMHFhI",
            "duration": "22 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.99,
            "view_count": "2.9M+ views",
            "level": "intermediate",
            "summary": "The highest-acclaimed machine learning teacher on the web. Visualizes bias vs variance, decision boundaries, and Gini impurity.",
            "key_takeaways": [
                "Bias (underfitting) vs Variance (overfitting) tradeoff in model training",
                "Decision trees recursively split features to minimize node impurity",
                "Random Forests aggregate multiple bootstrapped trees (bagging) to reduce variance",
                "Cross-validation prevents overfitting to test sets"
            ]
        },
        {
            "id": "vid_andrewng_ml_full",
            "title": "Supervised Machine Learning: Regression & Classification",
            "provider": "Andrew Ng (DeepLearning.AI / Stanford)",
            "video_url": "https://www.youtube.com/embed/k4pnz3bZg4E",
            "duration": "35 mins",
            "style": "comprehensive_masterclass",
            "creator_type": "global_goat",
            "rating": 4.99,
            "view_count": "3.2M+ views",
            "level": "beginner",
            "summary": "AI pioneer Andrew Ng introduces cost functions, gradient descent optimization, and classification metrics.",
            "key_takeaways": [
                "Cost function measures divergence between model predictions and ground truth labels",
                "Gradient descent iteratively updates parameters by moving against partial derivatives",
                "Learning rate hyperparameter controls step size and convergence",
                "Feature scaling (Z-score normalization) accelerates gradient descent convergence"
            ]
        }
    ],

    # 16. PyTorch & Neural Networks
    "pytorch_deep_learning": [
        {
            "id": "vid_karpathy_micrograd",
            "title": "Building micrograd & Neural Networks from Scratch: Zero to Hero",
            "provider": "Andrej Karpathy (Former Tesla AI / OpenAI)",
            "video_url": "https://www.youtube.com/embed/VMj-3S1tku0",
            "duration": "2.5 hours complete",
            "style": "comprehensive_masterclass",
            "creator_type": "global_goat",
            "rating": 4.99,
            "view_count": "4.1M+ views",
            "level": "intermediate",
            "summary": "Universally recognized as the greatest deep learning video in internet history. Builds backpropagation and PyTorch Autograd from scratch.",
            "key_takeaways": [
                "Backpropagation is recursive application of the calculus chain rule through a computational graph",
                "Tensors store multi-dimensional values and track computational history via grad_fn",
                "Forward pass computes loss; zero_grad() resets gradients; backward() computes dLoss/dW",
                "Optimizers (SGD, Adam) update weight tensors along negative gradients"
            ]
        },
        {
            "id": "vid_3b1b_neural_net",
            "title": "What is a Neural Network? | Chapter 1, Deep Learning",
            "provider": "3Blue1Brown",
            "video_url": "https://www.youtube.com/embed/aircAruvnKk",
            "duration": "19 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.99,
            "view_count": "18M+ views",
            "level": "beginner",
            "summary": "Unmatched mathematical animations explaining neurons, activations, weights, biases, and matrix transformations.",
            "key_takeaways": [
                "A neuron is a mathematical holding cell for a number between 0 and 1",
                "Weighted sum + bias passed through non-linear activation (ReLU, Sigmoid)",
                "Hidden layers extract hierarchical representations from raw inputs to abstract concepts",
                "Matrix multiplication accelerates parallel neural forward passes on GPUs"
            ]
        }
    ],

    # 17. Generative AI, RAG & Vector Databases
    "rag_vector_db": [
        {
            "id": "vid_karpathy_llm_intro",
            "title": "Intro to Large Language Models & Vector Retrieval",
            "provider": "Andrej Karpathy",
            "video_url": "https://www.youtube.com/embed/zjkBMFhNj_g",
            "duration": "55 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.99,
            "view_count": "3.5M+ views",
            "level": "intermediate",
            "summary": "Andrej Karpathy breaks down how LLMs are trained, tokenization, hallucinations, context windows, and Retrieval-Augmented Generation.",
            "key_takeaways": [
                "LLMs are statistical text generators trained on next-token prediction",
                "RAG grounds model responses in private documents without expensive retraining",
                "Embeddings map semantic text meaning into high-dimensional geometric vectors",
                "Vector databases (Pinecone, Chroma, Milvus) perform approximate nearest neighbor (ANN) cosine similarity search"
            ]
        },
        {
            "id": "vid_chai_rag_hindi",
            "title": "Complete RAG & Vector Databases Masterclass in Hindi",
            "provider": "Chai aur Code (Hitesh Choudhary)",
            "video_url": "https://www.youtube.com/embed/uD31q1a-pP4",
            "duration": "48 mins",
            "style": "hinglish_regional",
            "creator_type": "hinglish_goat",
            "rating": 4.97,
            "view_count": "450K+ views",
            "level": "beginner",
            "summary": "Hitesh demonstrates chunking, embedding generation with Ollama & HuggingFace, storing in vector stores, and building AI agents in Hindi.",
            "key_takeaways": [
                "Document chunking strategies: recursive character splitting with overlap",
                "Cosine similarity measures semantic angle distance between prompt and document chunks",
                "Augmenting prompts with retrieved context to eliminate hallucinations",
                "Building autonomous LLM tools and memory chains"
            ]
        }
    ],

    # 18. Tailwind CSS & Modern Design Systems
    "tailwind_css": [
        {
            "id": "vid_adam_tailwind_design",
            "title": "Designing with Tailwind CSS - Principles of Component Design",
            "provider": "Adam Wathan (Creator of Tailwind CSS)",
            "video_url": "https://www.youtube.com/embed/elgQt4z_Gf0",
            "duration": "28 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.98,
            "view_count": "1.3M+ views",
            "level": "intermediate",
            "summary": "The creator of Tailwind CSS demonstrates how to build reusable design tokens, manage whitespace, and avoid CSS bloat.",
            "key_takeaways": [
                "Utility-first classes eliminate naming fatigue and growing stylesheet sizes",
                "Design tokens enforce consistent scales for colors, typography, and spacing",
                "Component extraction pattern: React components encapsulate utility class combinations",
                "Just-In-Time (JIT) compiler generates only used CSS in production"
            ]
        },
        {
            "id": "vid_chai_tailwind_hindi",
            "title": "Tailwind CSS Complete Masterclass in Hindi",
            "provider": "Chai aur Code (Hitesh Choudhary)",
            "video_url": "https://www.youtube.com/embed/6i3EQPbiytw",
            "duration": "35 mins",
            "style": "hinglish_regional",
            "creator_type": "hinglish_goat",
            "rating": 4.97,
            "view_count": "920K+ views",
            "level": "beginner",
            "summary": "Hitesh walks through configuring Tailwind, responsive prefixes (sm, md, lg), dark mode toggles, and building sleek UI cards.",
            "key_takeaways": [
                "Responsive design using mobile-first utility prefixes",
                "Dark mode implementation using class strategy and CSS variables",
                "Hover, focus, and active interactive micro-state classes",
                "Customizing tailwind.config.ts with custom brand palettes"
            ]
        }
    ],

    # 19. TanStack Query & Server State
    "tanstack_query": [
        {
            "id": "vid_jack_tanstack_query",
            "title": "TanStack Query (React Query) v5: Why You Need It",
            "provider": "Jack Herrington & Tanner Linsley",
            "video_url": "https://www.youtube.com/embed/novnyCbeTxo",
            "duration": "24 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.97,
            "view_count": "580K+ views",
            "level": "intermediate",
            "summary": "Deep dive into server state vs client state, query keys, automatic refetching, deduplication, and optimistic mutations.",
            "key_takeaways": [
                "Server state is remote, asynchronous, and shared; client state is local and synchronous",
                "Query keys uniquely identify and cache remote data streams",
                "Deduplication prevents multiple identical requests from firing simultaneously",
                "Optimistic updates instantly update UI before the server mutation responds"
            ]
        },
        {
            "id": "vid_wds_react_query",
            "title": "React Query Crash Course",
            "provider": "Web Dev Simplified",
            "video_url": "https://www.youtube.com/embed/r8Dg0KVNFMA",
            "duration": "20 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.95,
            "view_count": "940K+ views",
            "level": "beginner",
            "summary": "Clear, accessible guide to useQuery, useMutation, staleTime, and cacheTime.",
            "key_takeaways": [
                "staleTime determines when cached data is considered stale and re-fetched in the background",
                "Automatic caching and garbage collection reduce network overhead",
                "useMutation handles POST, PUT, DELETE with onSuccess invalidation"
            ]
        }
    ],

    # 20. OWASP Top 10 & Web Cyber Security
    "owasp_security": [
        {
            "id": "vid_chuck_owasp",
            "title": "OWASP Top 10 Web Vulnerabilities Explained Live",
            "provider": "NetworkChuck",
            "video_url": "https://www.youtube.com/embed/2_lswM1S264",
            "duration": "25 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.98,
            "view_count": "2.2M+ views",
            "level": "beginner",
            "summary": "Chuck demonstrates hands-on exploitation and defense of SQL Injection, Broken Authentication, Cross-Site Scripting (XSS), and SSRF.",
            "key_takeaways": [
                "SQL Injection occurs when user input alters SQL query structure; solve with Parameterized Prepared Statements",
                "Cross-Site Scripting (XSS) injects malicious JavaScript into client browsers; solve with Context-Aware Escaping and CSP",
                "Broken Access Control allows unauthorized horizontal or vertical privilege escalation",
                "Content Security Policy (CSP) headers block unauthorized script and data exfiltration"
            ]
        },
        {
            "id": "vid_computerphile_sql_injection",
            "title": "SQL Injection & Cross Site Scripting Attacks in Depth",
            "provider": "Computerphile",
            "video_url": "https://www.youtube.com/embed/_jKylhJtPmI",
            "duration": "18 mins",
            "style": "architectural_deepdive",
            "creator_type": "global_goat",
            "rating": 4.97,
            "view_count": "3.1M+ views",
            "level": "intermediate",
            "summary": "Academic and industry security experts dissect memory buffers, input sanitation flaws, and defensive programming.",
            "key_takeaways": [
                "Never trust user input; always validate against strict white-lists on the server",
                "Principle of Least Privilege: database credentials should have minimal required permissions",
                "Security in depth: combining input sanitization, output encoding, and network firewalls"
            ]
        }
    ],

    # 21. Android & Jetpack Compose
    "android_compose": [
        {
            "id": "vid_philipp_compose_full",
            "title": "Jetpack Compose Full Course - Modern Android Development",
            "provider": "Philipp Lackner (Android Master)",
            "video_url": "https://www.youtube.com/embed/cDabx3SjuOY",
            "duration": "3 hours complete",
            "style": "comprehensive_masterclass",
            "creator_type": "global_goat",
            "rating": 4.98,
            "view_count": "1.2M+ views",
            "level": "beginner",
            "summary": "The definitive modern Android course replacing old XML layouts with declarative Kotlin Jetpack Compose UI, State hoisting, and ViewModels.",
            "key_takeaways": [
                "Composable functions declare UI reactively from current state",
                "remember and mutableStateOf preserve UI state across recomposition",
                "State hoisting separates UI rendering from business logic",
                "Clean Architecture with ViewModel, Repositories, and Kotlin Coroutines"
            ]
        },
        {
            "id": "vid_android_compose_official",
            "title": "Jetpack Compose Basics: Fast First Android App",
            "provider": "Android Developers (Official Google Team)",
            "video_url": "https://www.youtube.com/embed/6_wK4B34F6o",
            "duration": "18 mins",
            "style": "fastpaced_visual",
            "creator_type": "global_goat",
            "rating": 4.94,
            "view_count": "890K+ views",
            "level": "beginner",
            "summary": "Official tutorial building dynamic app screens, Material Design 3 theming, animations, and lists with LazyColumn.",
            "key_takeaways": [
                "LazyColumn provides high-performance virtualized scrolling lists",
                "Modifiers customize layout sizing, padding, background, and click interactions",
                "Material Theme provides dynamic dark/light color schemes out of the box"
            ]
        }
    ]
}


def match_topic_catalog_key(topic_id: str, title: str, domain: str = "") -> str:
    """
    Intelligently maps any topic_id, roadmap title, or domain to the optimal curated GOAT catalog key.
    """
    query = f"{topic_id} {title} {domain}".lower()

    if any(k in query for k in ["html", "css", "flexbox", "grid", "responsive", "semantic"]):
        return "html_css"
    elif any(k in query for k in ["react", "component", "hook", "jsx"]):
        return "react"
    elif any(k in query for k in ["next", "app_router", "ssr", "server_component"]):
        return "nextjs"
    elif any(k in query for k in ["fastapi", "rest", "endpoint", "api_design", "pydantic"]):
        return "fastapi"
    elif any(k in query for k in ["jwt", "auth", "security", "token", "hash", "password"]):
        return "auth"
    elif any(k in query for k in ["mongo", "nosql", "document", "bson"]):
        return "mongodb"
    elif any(k in query for k in ["docker", "container", "containerization", "dockerfile"]):
        return "docker"
    elif any(k in query for k in ["k8s", "kubernetes", "pod", "helm", "orchestrat"]):
        return "kubernetes"
    elif any(k in query for k in ["http", "protocol", "network", "dns", "tcp", "tls", "internet"]):
        return "http_networking"
    elif any(k in query for k in ["postgres", "sql", "relational", "database", "query"]):
        return "sql_postgres"
    elif any(k in query for k in ["redis", "cache", "caching", "in-memory"]):
        return "redis_caching"
    elif any(k in query for k in ["queue", "kafka", "rabbitmq", "celery", "broker", "event"]):
        return "queues_kafka"
    elif any(k in query for k in ["numpy", "pandas", "data science", "feature engineering"]):
        return "data_science_python"
    elif any(k in query for k in ["scikit", "classical_ml", "regression", "tree", "forest", "supervised"]):
        return "classical_ml"
    elif any(k in query for k in ["pytorch", "deep learning", "neural", "tensor", "backprop", "autograd"]):
        return "pytorch_deep_learning"
    elif any(k in query for k in ["rag", "vector", "embedding", "llm", "langchain", "generative"]):
        return "rag_vector_db"
    elif any(k in query for k in ["tailwind", "design system", "token", "ui/ux", "frontend"]):
        return "tailwind_css"
    elif any(k in query for k in ["tanstack", "react query", "query", "client state"]):
        return "tanstack_query"
    elif any(k in query for k in ["owasp", "cyber", "exploit", "hack", "penetration", "vulnerab"]):
        return "owasp_security"
    elif any(k in query for k in ["android", "compose", "kotlin", "mobile"]):
        return "android_compose"
    elif any(k in query for k in ["javascript", "es6", "event loop", "async", "promise", "closure"]):
        return "javascript"

    # Default fallback by domain
    if domain == "ai_ml":
        return "pytorch_deep_learning"
    elif domain == "backend":
        return "fastapi"
    elif domain == "devops":
        return "docker"
    elif domain == "cybersecurity":
        return "owasp_security"
    elif domain == "frontend":
        return "react"
    
    return "javascript"


def resolve_topic_videos(
    topic_id: str,
    title: str,
    domain: str = "",
    user_profile: Optional[Dict[str, Any]] = None,
    preferred_video_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Returns personalized GOAT educational videos for a topic.
    Includes:
    - active_lecture: The personalized best match (or user selected)
    - lectures: All curated options (Masterclass, Visual/Fast-Paced, Hinglish)
    - match_reason: Personalized explanation based on user's diagnostic profile
    """
    catalog_key = match_topic_catalog_key(topic_id, title, domain)
    options = CURATED_GOAT_CATALOG.get(catalog_key, CURATED_GOAT_CATALOG["javascript"])

    # Extract user profile signals
    user_level = "beginner"
    user_style = "visual"
    preferred_lang = "both"

    if user_profile:
        # Check assessment results or constraints
        user_level = user_profile.get("experience_level", "beginner")
        user_style = user_profile.get("learning_style", "visual")
        preferred_lang = user_profile.get("language_preference", "both")

    # Score each option against user preferences
    best_option = None
    highest_score = -1.0
    match_reason = "Selected as the highest-rated GOAT video for this topic"

    for opt in options:
        score = 0.0
        reasons = []

        # 1. Level match
        if opt.get("level") == user_level:
            score += 2.0
            reasons.append(f"Calibrated for your {user_level.title()} skill stage")
        else:
            score += 1.0

        # 2. Format / Style preference
        if user_style == "visual" and opt.get("style") in ["fastpaced_visual", "architectural_deepdive"]:
            score += 2.5
            reasons.append("Visual architecture diagrams match your cognitive learning preference")
        elif user_style == "comprehensive" and opt.get("style") == "comprehensive_masterclass":
            score += 2.5
            reasons.append("In-depth masterclass matches your comprehensive mastery pace")

        # 3. Language / Creator affinity
        if preferred_lang in ["hinglish", "hindi"] and opt.get("creator_type") == "hinglish_goat":
            score += 3.0
            reasons.append(f"Top Hinglish GOAT creator ({opt.get('provider')}) with 4.9+ rating")
        elif preferred_lang == "english" and opt.get("creator_type") == "global_goat":
            score += 2.0
            reasons.append(f"Global industry standard masterclass by {opt.get('provider')}")
        else:
            # Baseline high rating booster
            score += (opt.get("rating", 4.9) - 4.5) * 5.0

        # Specific video selected by user takes absolute priority
        if preferred_video_id and opt.get("id") == preferred_video_id:
            score += 100.0
            reasons = ["Your explicitly chosen learning resource"]

        if score > highest_score:
            highest_score = score
            best_option = opt
            match_reason = " • ".join(reasons) if reasons else f"Recommended GOAT resource by {opt.get('provider')}"

    if not best_option:
        best_option = options[0]

    # Return deep copies with personalized match tag
    resolved_lectures = []
    for opt in options:
        opt_copy = dict(opt)
        opt_copy["is_recommended"] = opt.get("id") == best_option.get("id")
        opt_copy["match_reason"] = match_reason if opt_copy["is_recommended"] else f"Alternative {opt.get('style', '').replace('_', ' ').title()} option"
        resolved_lectures.append(opt_copy)

    # Put best option first in the list
    resolved_lectures.sort(key=lambda x: 0 if x.get("is_recommended") else 1)

    return {
        "catalog_key": catalog_key,
        "recommended_lecture": resolved_lectures[0],
        "all_lectures": resolved_lectures,
        "match_reason": match_reason
    }
