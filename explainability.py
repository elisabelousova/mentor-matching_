def explain(mentor, mentee):
    reasons = []

    if mentor.get("domain") == mentee.get("domain"):
        reasons.append("совпадает профессиональная область")
    if mentor.get("skills") and mentee.get("skills") and set(mentor["skills"]) & set(mentee["skills"]):
        reasons.append("есть пересечение навыков")
    if mentor.get("goals") and mentee.get("goals") and set(mentor["goals"]) & set(mentee["goals"]):
        reasons.append("совпадают цели развития")
    if mentor.get("industry") == mentee.get("industry"):
        reasons.append("совпадает индустрия")

    if not reasons:
        return "рекомендация построена на суммарном совпадении нескольких признаков"
    return ", ".join(reasons)
