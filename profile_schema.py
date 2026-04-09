import random

DOMAINS = ["product", "analytics", "data_science", "ux", "engineering", "marketing"]

SKILLS = {
    "product": ["roadmap", "prioritization", "growth", "metrics"],
    "analytics": ["sql", "python", "dashboards", "ab_testing"],
    "data_science": ["ml", "python", "statistics", "nlp"],
    "ux": ["research", "interviews", "usability", "figma"],
    "engineering": ["backend", "api", "system_design", "testing"],
    "marketing": ["seo", "smm", "content", "ads"]
}

GOALS = {
    "product": ["growth", "strategy", "product_sense"],
    "analytics": ["advanced_sql", "experiments", "data_storytelling"],
    "data_science": ["deep_learning", "ml_projects", "modeling"],
    "ux": ["research_skills", "portfolio", "user_testing"],
    "engineering": ["scalability", "architecture", "performance"],
    "marketing": ["performance", "branding", "funnels"]
}

SENIORITY = ["junior", "middle", "senior", "lead", "head"]
FORMATS = ["online", "offline", "chat"]
INDUSTRIES = ["fintech", "ecommerce", "edtech", "saas"]

def random_profile(is_mentor=True):
    domain = random.choice(DOMAINS)
    skills = random.sample(SKILLS[domain], k=2)
    goals = random.sample(GOALS[domain], k=2)

    if is_mentor:
        seniority = random.choice(["senior", "lead", "head"])
    else:
        seniority = random.choice(["junior", "middle", "senior"])

    return {
        "domain": domain,
        "skills": skills,
        "goals": goals,
        "seniority": seniority,
        "format": random.choice(FORMATS),
        "industry": random.choice(INDUSTRIES),
    }
