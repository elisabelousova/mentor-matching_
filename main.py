import os
import pandas as pd

from data_generation import generate_data, save_json, mask_profile
from matching import match
from explainability import explain
from evaluation import run_fullness_experiment

def main():
    mentors, mentees = generate_data()

    os.makedirs("data/generated", exist_ok=True)
    os.makedirs("data/experiments", exist_ok=True)

    save_json(mentors, "data/generated/mentors.json")
    save_json(mentees, "data/generated/mentees.json")

    target_mentee = mentees[0]
    top_recommendations = match(mentors, target_mentee, k=3)

    print("Project run completed successfully.")
    print("Top-3 recommendations for mentee_1")
    recommendation_rows = []
    for idx, score in top_recommendations:
        mentor_name = f"mentor_{idx + 1}"
        print(f"- {mentor_name}: score={score}")
        recommendation_rows.append(
            {
                "mentee_id": "mentee_1",
                "mentor_id": mentor_name,
                "score": score,
                "explanation": explain(mentors[idx], target_mentee),
            }
        )

    rec_df = pd.DataFrame(recommendation_rows)
    rec_df.to_csv("data/experiments/example_recommendations.csv", index=False)

    fullness_df = run_fullness_experiment(mentors, mentees, mask_profile)
    fullness_df.to_csv("data/experiments/fullness_experiment.csv", index=False)

    print("\nAverage Precision@3 by profile fullness:")
    for _, row in fullness_df.iterrows():
        print(f"- fullness={row['fullness']}: AP@3={row['AP@3']}")

if __name__ == "__main__":
    main()
