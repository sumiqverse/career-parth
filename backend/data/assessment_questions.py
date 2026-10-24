# 15 Simple & Psychological Diagnostic Questions for Freshers & Beginners
# Designed to eliminate tutorial paralysis, jargon fear, and the "started 4 languages and quit" cycle.

ASSESSMENT_QUESTIONS = [
    {
        "id": 1,
        "question": "Think about your daily life. When do you get that sudden rush of satisfaction or excitement?",
        "category": "Natural Instinct",
        "options": [
            {
                "id": "q1_a",
                "text": "When I draw, design, or rearrange something and it visually looks clean, beautiful, and satisfying.",
                "domain_scores": {"frontend": 4, "fullstack": 2}
            },
            {
                "id": "q1_b",
                "text": "When I solve a tricky riddle, troubleshoot why a gadget is broken, or organize messy things into neat order.",
                "domain_scores": {"backend": 4, "fullstack": 2}
            },
            {
                "id": "q1_c",
                "text": "When I find a smarter shortcut, automate a boring repetitive task, or tweak computer/phone settings to make it faster.",
                "domain_scores": {"devops": 4, "backend": 2}
            },
            {
                "id": "q1_d",
                "text": "When I notice an interesting trend or pattern, or wonder 'How does Instagram know what I want to watch next?'",
                "domain_scores": {"ai_ml": 4}
            },
            {
                "id": "q1_idk",
                "text": "🤔 I honestly have no idea / Not sure yet (I haven't felt that technical excitement yet).",
                "is_idk": True,
                "domain_scores": {"fullstack": 1}
            }
        ]
    },
    {
        "id": 2,
        "question": "Be honest: Have you tried learning coding before (Python, C++, HTML, etc.)? What actually happened?",
        "category": "Past Experience",
        "options": [
            {
                "id": "q2_a",
                "text": "I watched YouTube tutorials or courses, but after a few days I got bored or felt lost because I didn't see where it was going.",
                "domain_scores": {"fullstack": 3, "frontend": 3}
            },
            {
                "id": "q2_b",
                "text": "I tried writing code, but when red errors appeared, I got discouraged because I couldn't see immediate visual results on screen.",
                "domain_scores": {"frontend": 4}
            },
            {
                "id": "q2_c",
                "text": "I enjoyed the logic puzzles, but the syntax memorization and heavy theory felt disconnected from building real apps.",
                "domain_scores": {"backend": 4, "fullstack": 2}
            },
            {
                "id": "q2_d",
                "text": "I'm an absolute beginner starting from zero — I've never touched code or opened a code editor.",
                "domain_scores": {"fullstack": 3}
            },
            {
                "id": "q2_idk",
                "text": "🤔 I started 3 or 4 things at once and quit because I thought 'maybe coding is not my type'.",
                "is_idk": True,
                "domain_scores": {"fullstack": 2}
            }
        ]
    },
    {
        "id": 3,
        "question": "If you were building a modern car with a team, which part would you naturally gravitate towards?",
        "category": "Mental Model",
        "options": [
            {
                "id": "q3_a",
                "text": "The interior dashboard, touchscreens, ambient lighting, and how smooth the steering feels to the driver.",
                "domain_scores": {"frontend": 4, "fullstack": 2}
            },
            {
                "id": "q3_b",
                "text": "The powerful engine, transmission, and fuel systems working quietly and reliably under the hood.",
                "domain_scores": {"backend": 4}
            },
            {
                "id": "q3_c",
                "text": "The autonomous self-driving cameras, sensors, and intelligent collision avoidance brain.",
                "domain_scores": {"ai_ml": 4}
            },
            {
                "id": "q3_d",
                "text": "The pit-crew operations: ensuring the car never breaks down, refuels in 2 seconds, and stays secure.",
                "domain_scores": {"devops": 4, "cybersecurity": 2}
            },
            {
                "id": "q3_idk",
                "text": "🤔 I don't know / I just want to see the whole car run and drive it around.",
                "is_idk": True,
                "domain_scores": {"fullstack": 2}
            }
        ]
    },
    {
        "id": 4,
        "question": "When you spend 45 minutes on a problem and it completely refuses to work, how does your brain react?",
        "category": "Frustration Tolerance",
        "options": [
            {
                "id": "q4_a",
                "text": "I lose energy quickly unless I can see visual feedback or break it into tiny, bite-sized mini-steps.",
                "domain_scores": {"frontend": 4}
            },
            {
                "id": "q4_b",
                "text": "I get stubborn like a detective! I want to isolate the exact reason why it broke and fix the root cause.",
                "domain_scores": {"backend": 4, "cybersecurity": 2}
            },
            {
                "id": "q4_c",
                "text": "I step back and search for a completely different angle, template, or creative workaround.",
                "domain_scores": {"fullstack": 4}
            },
            {
                "id": "q4_d",
                "text": "I get curious about whether other people face this issue and how top engineers automated a solution.",
                "domain_scores": {"devops": 3, "ai_ml": 3}
            },
            {
                "id": "q4_idk",
                "text": "🤔 I don't know / I usually close my laptop and feel overwhelmed, so I need gentle guidance.",
                "is_idk": True,
                "domain_scores": {"fullstack": 2}
            }
        ]
    },
    {
        "id": 5,
        "question": "When you use popular apps like Instagram, Spotify, or Uber, what catches your attention most?",
        "category": "Real-World Observation",
        "options": [
            {
                "id": "q5_a",
                "text": "The smooth page transitions, typography, button micro-animations, and how clean the interface feels.",
                "domain_scores": {"frontend": 4}
            },
            {
                "id": "q5_b",
                "text": "How they instantly match millions of rides or songs in milliseconds without losing your data or payments.",
                "domain_scores": {"backend": 4, "fullstack": 2}
            },
            {
                "id": "q5_c",
                "text": "How their recommendation engine accurately predicts what songs or reels match my exact mood.",
                "domain_scores": {"ai_ml": 4}
            },
            {
                "id": "q5_d",
                "text": "How the app stays online 24/7 without crashing even when millions of people open it at the same moment.",
                "domain_scores": {"devops": 4}
            },
            {
                "id": "q5_idk",
                "text": "🤔 I don't know / I just use them normally without thinking about the technical parts.",
                "is_idk": True,
                "domain_scores": {"fullstack": 1}
            }
        ]
    },
    {
        "id": 6,
        "question": "How do you genuinely feel when someone mentions 'Mathematics, Formulas, and Equations'?",
        "category": "Math Psychology",
        "options": [
            {
                "id": "q6_a",
                "text": "I don't like heavy math! I want to build practical digital apps without memorizing complex calculus formulas.",
                "domain_scores": {"frontend": 4, "fullstack": 3}
            },
            {
                "id": "q6_b",
                "text": "I'm comfortable with basic logic and rules (if this, then that), but prefer practical problem-solving.",
                "domain_scores": {"backend": 3, "cybersecurity": 2}
            },
            {
                "id": "q6_c",
                "text": "I actually find patterns, statistics, graphs, and probabilities fascinating when applied to real data.",
                "domain_scores": {"ai_ml": 5}
            },
            {
                "id": "q6_d",
                "text": "I care about system rules, checklists, and safety protocols rather than math equations.",
                "domain_scores": {"devops": 3, "cybersecurity": 3}
            },
            {
                "id": "q6_idk",
                "text": "🤔 I don't know / Math was taught poorly in school, so I don't know my true strength yet.",
                "is_idk": True,
                "domain_scores": {"fullstack": 2}
            }
        ]
    },
    {
        "id": 7,
        "question": "Which of these scenarios sounds most exciting to your personality?",
        "category": "Core Excitement",
        "options": [
            {
                "id": "q7_a",
                "text": "Building a full website or app from an empty screen and sending the link to my friends to test.",
                "domain_scores": {"fullstack": 4, "frontend": 2}
            },
            {
                "id": "q7_b",
                "text": "Finding a hidden loophole, bug, or security vulnerability and learning how to protect people from hackers.",
                "domain_scores": {"cybersecurity": 5}
            },
            {
                "id": "q7_c",
                "text": "Teaching a computer program to recognize human speech, translate languages, or generate smart answers.",
                "domain_scores": {"ai_ml": 4}
            },
            {
                "id": "q7_d",
                "text": "Building the underlying architecture that powers high-speed banking transactions or game servers.",
                "domain_scores": {"backend": 4}
            },
            {
                "id": "q7_idk",
                "text": "🤔 I don't know / All of them sound cool, but I have no idea which one I'd enjoy doing every day.",
                "is_idk": True,
                "domain_scores": {"fullstack": 2}
            }
        ]
    },
    {
        "id": 8,
        "question": "How long can you work on something without seeing any visible result before you lose interest?",
        "category": "Feedback Loop",
        "options": [
            {
                "id": "q8_a",
                "text": "15 to 30 minutes! I need to see whatever I just changed appear on screen right away to stay excited.",
                "domain_scores": {"frontend": 4}
            },
            {
                "id": "q8_b",
                "text": "A couple of hours is fine, as long as my tests pass or I can see that the logic works.",
                "domain_scores": {"backend": 4, "fullstack": 2}
            },
            {
                "id": "q8_c",
                "text": "I can be patient for days if I'm training an intelligent model or discovering deep insights.",
                "domain_scores": {"ai_ml": 4}
            },
            {
                "id": "q8_d",
                "text": "I enjoy automating pipelines so that once it's set up, everything works smoothly on its own forever.",
                "domain_scores": {"devops": 4}
            },
            {
                "id": "q8_idk",
                "text": "🤔 I don't know / My attention span gets drained easily if the tutorial is boring.",
                "is_idk": True,
                "domain_scores": {"fullstack": 2}
            }
        ]
    },
    {
        "id": 9,
        "question": "How does your brain absorb new concepts best without burning out?",
        "category": "Learning Style",
        "options": [
            {
                "id": "q9_a",
                "text": "I need hands-on practice right away. Watching 50 hours of slides makes my eyes glaze over.",
                "domain_scores": {"fullstack": 3, "frontend": 3}
            },
            {
                "id": "q9_b",
                "text": "I like clear visual roadmaps showing me Step 1, Step 2, Step 3 so I always know what's next.",
                "domain_scores": {"backend": 3, "fullstack": 3}
            },
            {
                "id": "q9_c",
                "text": "I learn best with gamification — streaks, XP points, and instant feedback when I pass a challenge.",
                "domain_scores": {"fullstack": 3, "frontend": 2}
            },
            {
                "id": "q9_d",
                "text": "I need simple real-world analogies (like recipes, plumbing, or legos) before any technical code.",
                "domain_scores": {"fullstack": 2, "backend": 2}
            },
            {
                "id": "q9_idk",
                "text": "🤔 I don't know / Nothing has worked consistently for me yet; I get stuck in tutorial hell.",
                "is_idk": True,
                "domain_scores": {"fullstack": 2}
            }
        ]
    },
    {
        "id": 10,
        "question": "When playing games or solving puzzles, which role do you naturally enjoy most?",
        "category": "Play Personality",
        "options": [
            {
                "id": "q10_a",
                "text": "The Creative Builder (crafting bases, customizing characters/skins, designing aesthetics).",
                "domain_scores": {"frontend": 4}
            },
            {
                "id": "q10_b",
                "text": "The Tactical Strategist (planning 5 moves ahead, optimizing inventory, solving puzzles).",
                "domain_scores": {"backend": 4}
            },
            {
                "id": "q10_c",
                "text": "The Curious Explorer (finding hidden secrets, testing game boundaries, searching for easter eggs).",
                "domain_scores": {"cybersecurity": 4, "ai_ml": 2}
            },
            {
                "id": "q10_d",
                "text": "The Support Orchestrator (keeping the team gear running, managing resources, zero bottlenecks).",
                "domain_scores": {"devops": 4}
            },
            {
                "id": "q10_idk",
                "text": "🤔 I don't know / I play casually or don't play games often.",
                "is_idk": True,
                "domain_scores": {"fullstack": 1}
            }
        ]
    },
    {
        "id": 11,
        "question": "Look at how you organize your physical room or digital phone/computer. Which sounds most like you?",
        "category": "Organization Archetype",
        "options": [
            {
                "id": "q11_a",
                "text": "Visually aesthetic: Clean wallpapers, color-coded themes, visually pleasing layout.",
                "domain_scores": {"frontend": 4}
            },
            {
                "id": "q11_b",
                "text": "Systematic: Clear folders, structured names, everything has an exact logical place.",
                "domain_scores": {"backend": 4}
            },
            {
                "id": "q11_c",
                "text": "Customizer: Custom shortcuts, developer settings tweaked, custom tools installed.",
                "domain_scores": {"devops": 4}
            },
            {
                "id": "q11_d",
                "text": "Creative chaos: It looks messy to others, but I know exactly where everything is in my head!",
                "domain_scores": {"fullstack": 4}
            },
            {
                "id": "q11_idk",
                "text": "🤔 I don't know / Just basic default settings, never really thought about it.",
                "is_idk": True,
                "domain_scores": {"fullstack": 1}
            }
        ]
    },
    {
        "id": 12,
        "question": "What has been the BIGGEST psychological hurdle holding you back in your tech journey so far?",
        "category": "The Core Blocker",
        "options": [
            {
                "id": "q12_a",
                "text": "Analysis Paralysis: Too much conflicting advice online ('Learn Python!', 'No, Web Dev!', 'No, C++!').",
                "domain_scores": {"fullstack": 4}
            },
            {
                "id": "q12_b",
                "text": "Imposter Syndrome: Feeling like other coders are naturally geniuses and I am starting too late.",
                "domain_scores": {"frontend": 2, "fullstack": 3}
            },
            {
                "id": "q12_c",
                "text": "Tutorial Hell: Watching video after video without ever being able to build a project on my own.",
                "domain_scores": {"fullstack": 4}
            },
            {
                "id": "q12_d",
                "text": "Getting Stuck on Errors: When code breaks, I have no clue where to look or what to do next.",
                "domain_scores": {"backend": 2, "fullstack": 3}
            },
            {
                "id": "q12_idk",
                "text": "🤔 I don't know / All of these feel true; I just need someone to hand me a clear roadmap.",
                "is_idk": True,
                "domain_scores": {"fullstack": 3}
            }
        ]
    },
    {
        "id": 13,
        "question": "If you could pick one tech superpower for your future self, which one would you choose?",
        "category": "Aspiration",
        "options": [
            {
                "id": "q13_a",
                "text": "The ability to build and launch complete web applications that anyone in the world can use.",
                "domain_scores": {"fullstack": 5}
            },
            {
                "id": "q13_b",
                "text": "The ability to architect ultra-fast, unbreakable systems that handle massive data with ease.",
                "domain_scores": {"backend": 5}
            },
            {
                "id": "q13_c",
                "text": "The ability to train and deploy intelligent AI models that understand text, images, and audio.",
                "domain_scores": {"ai_ml": 5}
            },
            {
                "id": "q13_d",
                "text": "The ability to protect systems, discover vulnerabilities, and defend against cyber attacks.",
                "domain_scores": {"cybersecurity": 5}
            },
            {
                "id": "q13_idk",
                "text": "🤔 I don't know / I just want to be confident that I'm learning the right high-demand skill.",
                "is_idk": True,
                "domain_scores": {"fullstack": 2}
            }
        ]
    },
    {
        "id": 14,
        "question": "Realistically, how much time can you comfortably commit to learning every day right now?",
        "category": "Time Reality",
        "options": [
            {
                "id": "q14_a",
                "text": "20 to 30 minutes a day (Micro-learning chunks so I never get burned out).",
                "domain_scores": {"frontend": 3, "fullstack": 2}
            },
            {
                "id": "q14_b",
                "text": "1 to 2 hours every evening (Steady, consistent habit with coding labs).",
                "domain_scores": {"fullstack": 3, "backend": 3}
            },
            {
                "id": "q14_c",
                "text": "3+ hours a day (Accelerated track, I want to transition careers quickly).",
                "domain_scores": {"backend": 3, "ai_ml": 3}
            },
            {
                "id": "q14_d",
                "text": "Mostly weekends (Deep focus blocks without weekday distractions).",
                "domain_scores": {"fullstack": 2, "devops": 2}
            },
            {
                "id": "q14_idk",
                "text": "🤔 I don't know / My college or work schedule changes every week.",
                "is_idk": True,
                "domain_scores": {"fullstack": 1}
            }
        ]
    },
    {
        "id": 15,
        "question": "One year from today, what result would make you feel truly proud and accomplished?",
        "category": "Your North Star",
        "options": [
            {
                "id": "q15_a",
                "text": "Having 3 real projects live on the internet that I built from scratch and can show recruiters.",
                "domain_scores": {"fullstack": 4, "frontend": 2}
            },
            {
                "id": "q15_b",
                "text": "Landing a high-paying, respected engineering job where I solve interesting backend challenges.",
                "domain_scores": {"backend": 4}
            },
            {
                "id": "q15_c",
                "text": "Being at the forefront of AI, building smart apps that leverage modern LLMs and data pipelines.",
                "domain_scores": {"ai_ml": 4}
            },
            {
                "id": "q15_d",
                "text": "Finally escaping tutorial paralysis and feeling like a confident, real software developer.",
                "domain_scores": {"fullstack": 4}
            },
            {
                "id": "q15_idk",
                "text": "🤔 I don't know / I just want to find something I enjoy and stop feeling clueless.",
                "is_idk": True,
                "domain_scores": {"fullstack": 2}
            }
        ]
    }
]

# Psychological Archetype & Domain Mapping
DOMAIN_DETAILS = {
    "fullstack": {
        "display_name": "Full Stack Product Builder",
        "archetype": "The All-Rounder Creator",
        "tagline": "Turn Any Idea into a Complete Live Digital Product",
        "psychological_summary": "You are naturally drawn to seeing the whole picture. Rather than getting stuck in isolated theory, your brain thrives on connecting the dots — designing the screen, handling the logic, and watching real people use what you created.",
        "why_it_fits": "Eliminates the 'I started Python and got lost' trap by giving you immediate visual wins in HTML/CSS/JS, followed step-by-step by backend and databases.",
        "primary_slug": "full-stack-developer"
    },
    "backend": {
        "display_name": "Backend & Systems Architect",
        "archetype": "The Systems Detective",
        "tagline": "Master the Invisible Engine Behind High-Speed Technology",
        "psychological_summary": "You have a natural analytical instinct. You enjoy puzzle solving, finding why something broke, and understanding how data flows quietly under the hood without getting distracted by surface colors.",
        "why_it_fits": "You won't get burned out by endless CSS tweaks; your dopamine comes from rock-solid API logic, databases, and green test checks.",
        "primary_slug": "backend-developer"
    },
    "ai_ml": {
        "display_name": "AI & Machine Learning Pioneer",
        "archetype": "The Intelligent Pattern Hunter",
        "tagline": "Build Smart Algorithms and Next-Gen AI Applications",
        "psychological_summary": "You are drawn to how systems think, predict, and adapt. You notice patterns in data, appreciate smart recommendations, and are inspired by the future of artificial intelligence.",
        "why_it_fits": "Bridges your natural curiosity about AI into practical hands-on Python projects, starting with intuitive concepts before any heavy math.",
        "primary_slug": "ai-ml-engineer"
    },
    "frontend": {
        "display_name": "Frontend & UI Craftsman",
        "archetype": "The Visual Craftsman",
        "tagline": "Design World-Class Interactive Experiences People Love",
        "psychological_summary": "Your brain craves instant visual feedback. You notice spacing, animations, typography, and human emotions when using an app. Making something feel smooth gives you an immediate rush of energy.",
        "why_it_fits": "Zero abstract frustration: every single line of code you write changes something right before your eyes in seconds.",
        "primary_slug": "frontend-developer"
    },
    "devops": {
        "display_name": "DevOps & Cloud Engineer",
        "archetype": "The Automation Optimizer",
        "tagline": "Keep Modern Clouds Running at Peak Performance 24/7",
        "psychological_summary": "You hate doing repetitive manual chores. You love shortcuts, clean automation, and ensuring that everything runs like clockwork with zero crashes.",
        "why_it_fits": "Focuses on high-leverage cloud tools (Docker, CI/CD, AWS) where you build systems that operate reliably forever.",
        "primary_slug": "devops-engineer"
    },
    "cybersecurity": {
        "display_name": "Cyber Defense & Security Sentinel",
        "archetype": "The Digital Sentinel",
        "tagline": "Uncover Hidden Vulnerabilities and Defend the Digital World",
        "psychological_summary": "You naturally think outside the box. You look at rules and wonder how they could be broken, and you care deeply about privacy, defense, and keeping systems safe.",
        "why_it_fits": "Turns your curiosity for breaking things and finding loopholes into an elite, high-demand defensive skill.",
        "primary_slug": "cyber-security"
    },
    "exploring": {
        "display_name": "The Curious Explorer Track",
        "archetype": "The Curious Explorer",
        "tagline": "Discover Your Technical Superpower at Your Own Pace",
        "psychological_summary": "You are completely honest with yourself: you don't know your exact lane yet, and that is 100% okay! Forcing you into a rigid box too early is why you abandoned Python, C++, or HTML in the past.",
        "why_it_fits": "We start you on an adaptive gateway path with quick, enjoyable micro-lessons. Horizon will ask you 5-second check-ins after each hands-on lab to dynamically uncover what your brain truly loves.",
        "primary_slug": "full-stack-developer"
    }
}

# Adaptive in-learning reflection questions that pop up during the course
ADAPTIVE_CHECKPOINTS = [
    {
        "id": "chk_html_visual",
        "trigger_topic": "fs_topic_html_css",
        "prompt": "🧠 Quick Brain Check: You just wrote your first styling and layout code. How did that feel?",
        "options": [
            {
                "id": "chk_1_loved",
                "text": "Loved it! Changing colors and seeing buttons move on screen gave me an instant rush.",
                "reinforce_domain": "frontend"
            },
            {
                "id": "chk_1_logic_craving",
                "text": "It was okay, but I find myself craving real logic, calculations, and data behind the scenes.",
                "reinforce_domain": "backend"
            },
            {
                "id": "chk_1_curious",
                "text": "Still exploring, but I enjoyed following clear guided steps without getting lost.",
                "reinforce_domain": "fullstack"
            }
        ]
    },
    {
        "id": "chk_js_logic",
        "trigger_topic": "fs_topic_js_es6",
        "prompt": "🧠 Quick Brain Check: You just explored functions and asynchronous code. How did the logic puzzle feel?",
        "options": [
            {
                "id": "chk_2_puzzle_fun",
                "text": "Fascinating! Figuring out how data flows and functions work together felt like solving a cool puzzle.",
                "reinforce_domain": "backend"
            },
            {
                "id": "chk_2_visual_pull",
                "text": "I enjoyed it, but I want to connect this logic directly to make visual web components react.",
                "reinforce_domain": "fullstack"
            },
            {
                "id": "chk_2_ai_curiosity",
                "text": "I want to see how this connects to training smart models and intelligent agents.",
                "reinforce_domain": "ai_ml"
            }
        ]
    }
]
