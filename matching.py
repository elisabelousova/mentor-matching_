SENIORITY_MAP = {
    "junior": 1,
    "middle": 2,
    "senior": 3,
    "lead": 4,
    "head": 5,
}

def jaccard(a, b):
    if not a or not b:
        return 0.0
    a, b = set(a), set(b)
    union = a | b
    if not union:
        return 0.0
    return len(a & b) / len(union)

def seniority_score(mentor_level, mentee_level):
    if not mentor_level or not mentee_level:
        return 0.0
    return 1.0 if SENIORITY_MAP[mentor_level] >= SENIORITY_MAP[mentee_level] else 0.0

def compute_score(mentor, mentee):
    domain = 1.0 if mentor.get("domain") and mentor.get("domain") == mentee.get("domain") else 0.0
    skills = jaccard(mentor.get("skills"), mentee.get("skills"))
    goals = jaccard(mentor.get("goals"), mentee.get("goals"))
    seniority = seniority_score(mentor.get("seniority"), mentee.get("seniority"))
    format_fit = 1.0 if mentor.get("format") and mentor.get("format") == mentee.get("format") else 0.0
    industry = 1.0 if mentor.get("industry") and mentor.get("industry") == mentee.get("industry") else 0.0

    score = (
        0.25 * domain
        + 0.20 * skills
        + 0.20 * goals
        + 0.10 * seniority
        + 0.10 * format_fit
        + 0.15 * industry
    )
    return round(score, 4)

def match(mentors, mentee, k=3):
    scored = [(idx, compute_score(mentor, mentee)) for idx, mentor in enumerate(mentors)]
    ranked = sorted(scored, key=lambda x: x[1], reverse=True)
    return ranked[:k]
