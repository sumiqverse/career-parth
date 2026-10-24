from typing import Dict, List, Any
from data.assessment_questions import ASSESSMENT_QUESTIONS, DOMAIN_DETAILS
from data.seed_roadmaps import SEED_ROADMAPS

def compute_assessment_result(answers: Dict[str, str]) -> Dict[str, Any]:
    """
    Computes domain affinity scores based on user answers to the 15 diagnostic questions,
    identifies the optimal primary domain, and ranks the Top 4 personalized roadmaps.
    """
    # Initialize domain scores
    domain_scores: Dict[str, int] = {
        "fullstack": 0,
        "backend": 0,
        "ai_ml": 0,
        "frontend": 0,
        "devops": 0,
        "cybersecurity": 0
    }

    # Map question id to options
    question_map = {q["id"]: {opt["id"]: opt for opt in q["options"]} for q in ASSESSMENT_QUESTIONS}

    for q_id_str, opt_id in answers.items():
        try:
            q_id = int(q_id_str)
        except ValueError:
            continue

        if q_id in question_map and opt_id in question_map[q_id]:
            selected_option = question_map[q_id][opt_id]
            scores = selected_option.get("domain_scores", {})
            for domain, points in scores.items():
                if domain in domain_scores:
                    domain_scores[domain] += points

    # Find winning domain (if all 0, default to fullstack)
    sorted_domains = sorted(domain_scores.items(), key=lambda x: x[1], reverse=True)
    top_domain = sorted_domains[0][0] if sorted_domains and sorted_domains[0][1] > 0 else "fullstack"
    domain_info = DOMAIN_DETAILS.get(top_domain, DOMAIN_DETAILS["fullstack"])

    # Rank the Top 4 roadmaps based on domain affinity
    # Prioritize the primary domain roadmap, followed by next highest scoring domains
    roadmap_rankings = []
    ranked_domain_keys = [d[0] for d in sorted_domains]

    # Map domain to roadmap
    domain_to_roadmap = {rm["domain"]: rm for rm in SEED_ROADMAPS}

    # Add primary domain roadmap first
    if top_domain in domain_to_roadmap:
        roadmap_rankings.append(domain_to_roadmap[top_domain])

    # Add remaining roadmaps in order of domain score
    for d_key in ranked_domain_keys:
        if d_key != top_domain and d_key in domain_to_roadmap:
            roadmap_rankings.append(domain_to_roadmap[d_key])

    # If still fewer than 4, append remaining
    for rm in SEED_ROADMAPS:
        if rm not in roadmap_rankings:
            roadmap_rankings.append(rm)

    top_4_roadmaps = roadmap_rankings[:4]

    return {
        "recommended_domain": top_domain,
        "domain_display_name": domain_info["display_name"],
        "tagline": domain_info["tagline"],
        "description": domain_info["description"],
        "primary_slug": domain_info["primary_slug"],
        "domain_scores": domain_scores,
        "top_roadmaps": top_4_roadmaps
    }
