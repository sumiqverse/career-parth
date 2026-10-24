# 15 Diagnostic Questions mapping cognitive style, interests, and background to tech domains

ASSESSMENT_QUESTIONS = [
    {
        "id": 1,
        "question": "When working on a digital project, which part excites you the most?",
        "category": "Interests",
        "options": [
            {
                "id": "q1_a",
                "text": "Designing sleek, responsive user interfaces with smooth animations",
                "domain_scores": {"frontend": 4, "fullstack": 2}
            },
            {
                "id": "q1_b",
                "text": "Architecting database schemas, business logic, and fast APIs",
                "domain_scores": {"backend": 4, "fullstack": 2}
            },
            {
                "id": "q1_c",
                "text": "Training smart models that can recognize patterns or generate insights",
                "domain_scores": {"ai_ml": 4}
            },
            {
                "id": "q1_d",
                "text": "Automating cloud deployments, servers, and zero-downtime infrastructure",
                "domain_scores": {"devops": 4}
            }
        ]
    },
    {
        "id": 2,
        "question": "How comfortable do you feel with mathematical concepts like linear algebra, statistics, and calculus?",
        "category": "Foundations",
        "options": [
            {
                "id": "q2_a",
                "text": "I enjoy math and love working with statistics, probabilities, and matrix math",
                "domain_scores": {"ai_ml": 4}
            },
            {
                "id": "q2_b",
                "text": "I like discrete math and logic, but prefer practical algorithmic problem-solving",
                "domain_scores": {"backend": 3, "cybersecurity": 2}
            },
            {
                "id": "q2_c",
                "text": "Basic math is fine, but I prefer spatial reasoning, layouts, and visual design",
                "domain_scores": {"frontend": 4, "fullstack": 2}
            },
            {
                "id": "q2_d",
                "text": "I care more about systems stability, networking configs, and terminal tools",
                "domain_scores": {"devops": 4}
            }
        ]
    },
    {
        "id": 3,
        "question": "If you saw an unexpected error message in production, what is your instinct?",
        "category": "Problem Solving",
        "options": [
            {
                "id": "q3_a",
                "text": "Check browser developer tools, CSS layouts, and UI console errors",
                "domain_scores": {"frontend": 4}
            },
            {
                "id": "q3_b",
                "text": "Inspect server logs, database query latency, and API payload contracts",
                "domain_scores": {"backend": 4, "fullstack": 2}
            },
            {
                "id": "q3_c",
                "text": "Inspect Docker container metrics, Kubernetes pods, and CI/CD pipelines",
                "domain_scores": {"devops": 4}
            },
            {
                "id": "q3_d",
                "text": "Check security logs, unauthorized token access, or packet anomalies",
                "domain_scores": {"cybersecurity": 4}
            }
        ]
    },
    {
        "id": 4,
        "question": "Which type of project would you be proudest to show on your portfolio?",
        "category": "Goals",
        "options": [
            {
                "id": "q4_a",
                "text": "A full end-to-end web app like Airbnb or Notion that users can sign up and use",
                "domain_scores": {"fullstack": 4, "frontend": 2, "backend": 2}
            },
            {
                "id": "q4_b",
                "text": "An AI-powered document search engine utilizing LLMs and vector embeddings",
                "domain_scores": {"ai_ml": 4, "backend": 2}
            },
            {
                "id": "q4_c",
                "text": "A high-performance banking transaction engine processing 50k requests/sec",
                "domain_scores": {"backend": 4}
            },
            {
                "id": "q4_d",
                "text": "A multi-cloud automated deployment pipeline using Terraform and Kubernetes",
                "domain_scores": {"devops": 4}
            }
        ]
    },
    {
        "id": 5,
        "question": "How do you feel about working extensively in the command line / Linux terminal?",
        "category": "Tools",
        "options": [
            {
                "id": "q5_a",
                "text": "I love the terminal! Bash scripts, SSH keys, vim, and CLI tools feel natural",
                "domain_scores": {"devops": 4, "cybersecurity": 3, "backend": 2}
            },
            {
                "id": "q5_b",
                "text": "I use the terminal when necessary (git, npm, docker), but prefer a graphical IDE",
                "domain_scores": {"fullstack": 3, "backend": 2}
            },
            {
                "id": "q5_c",
                "text": "I prefer visual tools, browser previews, Figma, and immediate visual feedback",
                "domain_scores": {"frontend": 4}
            },
            {
                "id": "q5_d",
                "text": "I primarily use Jupyter Notebooks, Google Colab, and Python scripts",
                "domain_scores": {"ai_ml": 4}
            }
        ]
    },
    {
        "id": 6,
        "question": "What is your stance on learning and testing security vulnerabilities?",
        "category": "Specialization",
        "options": [
            {
                "id": "q6_a",
                "text": "Fascinated! I want to understand SQL injections, XSS, packet sniffing, and penetration testing",
                "domain_scores": {"cybersecurity": 5}
            },
            {
                "id": "q6_b",
                "text": "Important, but I focus on securing my APIs with JWT, OAuth, and rate limiting",
                "domain_scores": {"backend": 3, "fullstack": 2}
            },
            {
                "id": "q6_c",
                "text": "I care about secure cloud IAM roles, VPC firewalls, and container vulnerability scanning",
                "domain_scores": {"devops": 4}
            },
            {
                "id": "q6_d",
                "text": "I prioritize clean user input validation and accessible UI security",
                "domain_scores": {"frontend": 3}
            }
        ]
    },
    {
        "id": 7,
        "question": "Which programming language feels most appealing or familiar to you?",
        "category": "Languages",
        "options": [
            {
                "id": "q7_a",
                "text": "JavaScript / TypeScript (React, Next.js, Node.js)",
                "domain_scores": {"frontend": 3, "fullstack": 4}
            },
            {
                "id": "q7_b",
                "text": "Python (Data science, PyTorch, FastAPI, Automation)",
                "domain_scores": {"ai_ml": 4, "backend": 2}
            },
            {
                "id": "q7_c",
                "text": "Go / Rust / Java (High concurrency, microservices, system efficiency)",
                "domain_scores": {"backend": 4, "devops": 2}
            },
            {
                "id": "q7_d",
                "text": "YAML, Bash, Python, and HCL (Terraform)",
                "domain_scores": {"devops": 4}
            }
        ]
    },
    {
        "id": 8,
        "question": "How important is immediate visual gratification while you code?",
        "category": "Feedback Loop",
        "options": [
            {
                "id": "q8_a",
                "text": "Critical! I want to refresh the browser and instantly see colors, cards, and layouts update",
                "domain_scores": {"frontend": 5}
            },
            {
                "id": "q8_b",
                "text": "Moderate. A clean green test suite or 200 OK Postman response gives me that same thrill",
                "domain_scores": {"backend": 4, "fullstack": 2}
            },
            {
                "id": "q8_c",
                "text": "I love watching training loss decrease on a tensorboard chart over 50 epochs",
                "domain_scores": {"ai_ml": 5}
            },
            {
                "id": "q8_d",
                "text": "A green CI/CD build passing in GitHub Actions gives me the biggest dopamine hit",
                "domain_scores": {"devops": 5}
            }
        ]
    },
    {
        "id": 9,
        "question": "Which of these real-world challenges sounds most thrilling to solve?",
        "category": "Impact",
        "options": [
            {
                "id": "q9_a",
                "text": "Making a heavy webpage load in under 1 second with 60fps animations on mobile",
                "domain_scores": {"frontend": 4}
            },
            {
                "id": "q9_b",
                "text": "Preventing a database deadlock during Black Friday peak shopping hours",
                "domain_scores": {"backend": 4}
            },
            {
                "id": "q9_c",
                "text": "Fine-tuning an open-source LLM to accurately answer medical or legal questions",
                "domain_scores": {"ai_ml": 4}
            },
            {
                "id": "q9_d",
                "text": "Simulating a DDoS attack and setting up Cloudflare/WAF rules to repel it",
                "domain_scores": {"cybersecurity": 4, "devops": 2}
            }
        ]
    },
    {
        "id": 10,
        "question": "When building an application, would you rather wear all the hats or go deep into one domain?",
        "category": "Scope",
        "options": [
            {
                "id": "q10_a",
                "text": "I want to be a versatile Swiss Army knife: build the frontend, backend, and deploy it all",
                "domain_scores": {"fullstack": 5}
            },
            {
                "id": "q10_b",
                "text": "I want to go deep into backend logic, database optimization, and high-scale architecture",
                "domain_scores": {"backend": 4}
            },
            {
                "id": "q10_c",
                "text": "I want to master UI engineering, interaction design, accessibility, and web performance",
                "domain_scores": {"frontend": 4}
            },
            {
                "id": "q10_d",
                "text": "I want to specialize in cutting-edge AI, neural models, and data pipelines",
                "domain_scores": {"ai_ml": 4}
            }
        ]
    },
    {
        "id": 11,
        "question": "What is your experience level with writing code so far?",
        "category": "Background",
        "options": [
            {
                "id": "q11_a",
                "text": "Absolute beginner — starting from zero with high curiosity",
                "domain_scores": {"frontend": 3, "fullstack": 2}
            },
            {
                "id": "q11_b",
                "text": "I know basic syntax (variables, loops, functions) and built a couple of basic scripts",
                "domain_scores": {"fullstack": 3, "backend": 2}
            },
            {
                "id": "q11_c",
                "text": "Intermediate — I understand APIs, Git, and have built simple web or data apps",
                "domain_scores": {"backend": 3, "ai_ml": 2, "fullstack": 3}
            },
            {
                "id": "q11_d",
                "text": "Experienced programmer looking to transition into modern cloud or AI technologies",
                "domain_scores": {"ai_ml": 3, "devops": 3}
            }
        ]
    },
    {
        "id": 12,
        "question": "How do you feel about working with databases like PostgreSQL, MongoDB, or Redis?",
        "category": "Databases",
        "options": [
            {
                "id": "q12_a",
                "text": "Excited! Designing relational tables, indexing, caching, and writing complex queries sounds fun",
                "domain_scores": {"backend": 4, "fullstack": 2}
            },
            {
                "id": "q12_b",
                "text": "I want to use Vector Databases (Pinecone, ChromaDB) to store high-dimensional embeddings",
                "domain_scores": {"ai_ml": 4}
            },
            {
                "id": "q12_c",
                "text": "I just need a clean ORM or API endpoint so I can focus on rendering data nicely in the UI",
                "domain_scores": {"frontend": 4}
            },
            {
                "id": "q12_d",
                "text": "I care about database replication, sharding, automated backups, and multi-region failovers",
                "domain_scores": {"devops": 4}
            }
        ]
    },
    {
        "id": 13,
        "question": "Which tech company's engineering challenge sounds coolest to you?",
        "category": "Industry",
        "options": [
            {
                "id": "q13_a",
                "text": "OpenAI / Anthropic: Scaling model inference, attention mechanisms, and agentic workflows",
                "domain_scores": {"ai_ml": 5}
            },
            {
                "id": "q13_b",
                "text": "Stripe / Uber: Architecting distributed payment systems with zero data corruption",
                "domain_scores": {"backend": 4, "fullstack": 2}
            },
            {
                "id": "q13_c",
                "text": "Linear / Figma: Building world-class, keyboard-first, ultra-responsive web experiences",
                "domain_scores": {"frontend": 4, "fullstack": 2}
            },
            {
                "id": "q13_d",
                "text": "Cloudflare / AWS: Running globally distributed edge networks and stopping cyber attacks",
                "domain_scores": {"devops": 3, "cybersecurity": 4}
            }
        ]
    },
    {
        "id": 14,
        "question": "How many hours per week can you dedicate to hands-on skill building?",
        "category": "Commitment",
        "options": [
            {
                "id": "q14_a",
                "text": "3–5 hours / week (Quick micro-lessons, focused roadmaps, high efficiency)",
                "domain_scores": {"frontend": 2, "fullstack": 1}
            },
            {
                "id": "q14_b",
                "text": "5–10 hours / week (Balanced pace with coding labs and workshops)",
                "domain_scores": {"fullstack": 2, "backend": 2}
            },
            {
                "id": "q14_c",
                "text": "10–20 hours / week (Deep dive with complex projects and capstones)",
                "domain_scores": {"fullstack": 3, "backend": 3, "ai_ml": 2}
            },
            {
                "id": "q14_d",
                "text": "20+ hours / week (Intensive immersion ready to master tough architectures)",
                "domain_scores": {"ai_ml": 3, "backend": 3, "devops": 3}
            }
        ]
    },
    {
        "id": 15,
        "question": "What is your primary goal over the next 3 to 6 months?",
        "category": "Career Vision",
        "options": [
            {
                "id": "q15_a",
                "text": "Build and launch my own SaaS / startup product independently",
                "domain_scores": {"fullstack": 5}
            },
            {
                "id": "q15_b",
                "text": "Land a high-paying software engineering job at a tech company",
                "domain_scores": {"backend": 3, "fullstack": 3}
            },
            {
                "id": "q15_c",
                "text": "Become a modern AI / Machine Learning practitioner building generative apps",
                "domain_scores": {"ai_ml": 5}
            },
            {
                "id": "q15_d",
                "text": "Specialize in high-demand Cloud, DevOps, or Cyber Defense infrastructure",
                "domain_scores": {"devops": 4, "cybersecurity": 4}
            }
        ]
    }
]

DOMAIN_DETAILS = {
    "fullstack": {
        "display_name": "Full Stack Web Development",
        "tagline": "The Complete Product Builder",
        "description": "You thrive when building complete products from end to end. From dynamic frontend components to robust APIs, databases, and deployment pipelines, you have the entrepreneurial mindset to turn ideas into live web apps.",
        "primary_slug": "full-stack-developer"
    },
    "backend": {
        "display_name": "Backend & Systems Engineering",
        "tagline": "The Architectural Mastermind",
        "description": "You love systems logic, high performance, and reliability. Designing clean REST & GraphQL APIs, caching layers, microservices, and database schemas is where you shine.",
        "primary_slug": "backend-developer"
    },
    "ai_ml": {
        "display_name": "AI & Machine Learning Engineering",
        "tagline": "The Intelligence Innovator",
        "description": "You are drawn to data, patterns, and intelligent systems. From foundational Python and PyTorch to modern LLM agents, RAG pipelines, and vector databases, you are building the future.",
        "primary_slug": "ai-ml-engineer"
    },
    "frontend": {
        "display_name": "Frontend & UI/UX Engineering",
        "tagline": "The Visual & Interactive Craftsman",
        "description": "You care deeply about user experience, fluid animations, typography, and web performance. You bridge the gap between design and interactive code using React, Next.js, and CSS masterclass.",
        "primary_slug": "frontend-developer"
    },
    "devops": {
        "display_name": "DevOps & Cloud Architecture",
        "tagline": "The Reliability & Infrastructure Leader",
        "description": "You believe in automation, uptime, and scalable clouds. Mastering Docker, Kubernetes, CI/CD, AWS, and Infrastructure-as-Code makes you indispensable to high-growth tech teams.",
        "primary_slug": "devops-engineer"
    },
    "cybersecurity": {
        "display_name": "Cyber Security & Defense",
        "tagline": "The Digital Sentinel & Ethical Hacker",
        "description": "You think like an attacker to build unbreakable shields. Network security, web application penetration testing, cryptographic systems, and threat mitigation are your super-powers.",
        "primary_slug": "cyber-security"
    }
}
