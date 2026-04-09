import pandas as pd
from matching import match

def is_relevant(mentor, mentee):
    if mentor.get("domain") != mentee.get("domain"):
        return False
    skills_overlap = bool(set(mentor.get("skills", [])) & set(mentee.get("skills", []) or []))
    goals_overlap = bool(set(mentor.get("goals", [])) & set(mentee.get("goals", []) or []))
    return skills_overlap or goals_overlap

def precision_at_k(mentors, mentees, k=3):
    values = []
    for mentee in mentees:
        top_k = match(mentors, mentee, k=k)
        relevant_count = sum(1 for idx, _ in top_k if is_relevant(mentors[idx], mentee))
        values.append(relevant_count / k)
    return round(sum(values) / len(values), 4)

def run_fullness_experiment(mentors, mentees, mask_fn):
    rows = []
    for fullness in [1.0, 0.75, 0.5, 0.25]:
        masked_mentees = [mask_fn(mentee, fullness) for mentee in mentees]
        ap3 = precision_at_k(mentors, masked_mentees, k=3)
        rows.append({"fullness": fullness, "AP@3": ap3})
    return pd.DataFrame(rows)
