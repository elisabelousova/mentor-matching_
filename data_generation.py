import json
import random
from profile_schema import random_profile

def generate_data(n_mentors=100, n_mentees=30):
    mentors = [random_profile(True) for _ in range(n_mentors)]
    mentees = [random_profile(False) for _ in range(n_mentees)]
    return mentors, mentees

def mask_profile(profile, fullness=1.0):
    masked = {}
    for key, value in profile.items():
        masked[key] = value if random.random() <= fullness else None
    return masked

def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
