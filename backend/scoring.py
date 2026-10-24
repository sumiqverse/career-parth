from typing import Dict, List, Any
from data.assessment_questions import ASSESSMENT_QUESTIONS, DOMAIN_DETAILS
from data.seed_roadmaps import SEED_ROADMAPS

def compute_assessment_result(answers: Dict[str, str]) -> Dict[str, Any]:
    """
    Computes domain affinity scores based on user answers to the 15 diagnostic questions,
    identifies the optimal psychological archetype, and ranks the Top 4 personalized roadmaps.
    Handles 'I don't know' (IDK) responses with the compassionate 'Curious Explorer' adaptive track.
    """
    domain_scores: Dict[str, int] = {
        "fullstack": 0,
        "backend": 0,
        "ai_ml": 0,
        "frontend": 0,
        "devops": 0,
        "cybersecurity": 0
    }

    idk_count = 0

    # Map question id to options
    question_map = {q["id"]: {opt["id"]: opt for opt in q["options"]} for q in ASSESSMENT_QUESTIONS}

    for q_id_str, opt_id in answers.items():
        try:
            q_id = int(q_id_str)
        except ValueError:
            continue

        if q_id in question_map and opt_id in question_map[q_id]:
            selected_option = question_map[q_id][opt_id]
            
            # Check if this option is an "I don't know" option
            if selected_option.get("is_idk") or opt_id.endswith("_idk"):
                idk_count += 1

            scores = selected_option.get("domain_scores", {})
            for domain, points in scores.items():
                if domain in domain_scores:
                    domain_scores[domain] += points

    # If the user selected mostly "I don't know" (>= 5 questions), classify as Curious Explorer
    if idk_count >= 5:
        top_domain = "exploring"
        domain_info = DOMAIN_DETAILS["exploring"]
    else:
        # Find winning domain from scores
        sorted_domains = sorted(domain_scores.items(), key=lambda x: x[1], reverse=True)
        top_domain = sorted_domains[0][0] if sorted_domains and sorted_domains[0][1] > 0 else "fullstack"
        domain_info = DOMAIN_DETAILS.get(top_domain, DOMAIN_DETAILS["fullstack"])

    # Rank the Top 4 roadmaps based on domain affinity
    # Prioritize the primary domain roadmap, followed by next highest scoring domains
    roadmap_rankings = []
    
    # Map domain to roadmap
    domain_to_roadmap = {rm["domain"]: rm for rm in SEED_ROADMAPS}

    target_primary_slug = domain_info.get("primary_slug", "full-stack-developer")
    
    # Find matching primary roadmap
    primary_rm = next((rm for rm in SEED_ROADMAPS if rm["slug"] == target_primary_slug), SEED_ROADMAPS[0])
    roadmap_rankings.append(primary_rm)

    # Rank remainder by domain score
    sorted_domains_list = sorted(domain_scores.items(), key=lambda x: x[1], reverse=True)
    for d_key, _ in sorted_domains_list:
        if d_key in domain_to_roadmap:
            candidate = domain_to_roadmap[d_key]
            if candidate not in roadmap_rankings:
                roadmap_rankings.append(candidate)

    # Fill up to 4
    for rm in SEED_ROADMAPS:
        if rm not in roadmap_rankings:
            roadmap_rankings.append(rm)

    top_4_roadmaps = roadmap_rankings[:4]

    return {
        "recommended_domain": top_domain,
        "domain_display_name": domain_info["display_name"],
        "archetype": domain_info.get("archetype", "The Software Craftsman"),
        "tagline": domain_info["tagline"],
        "description": domain_info.get("psychological_summary", ""),
        "why_it_fits": domain_info.get("why_it_fits", ""),
        "primary_slug": domain_info["primary_slug"],
        "idk_count": idk_count,
        "is_exploring_mode": top_domain == "exploring",
        "domain_scores": domain_scores,
        "top_roadmaps": top_4_roadmaps
    }
