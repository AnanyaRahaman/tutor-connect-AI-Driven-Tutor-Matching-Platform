import joblib
import pandas as pd

from ai_engine.utils import subject_match, price_difference, availability_score

model = joblib.load("ai_engine/ml_models/tutor_model.pkl")


def recommend_tutors(student, tutors):

    results = []

    for tutor in tutors:

        features = {
            "subject_match": subject_match(student["subject"], tutor["subject"]),
            "rating": tutor["rating"],
            "price_diff": price_difference(student["budget"], tutor["price"]),
            "availability": availability_score(tutor["available"]),
            "experience": tutor["experience"]
        }

        df = pd.DataFrame([features])

        probability = model.predict_proba(df)[0][1]

        tutor["match_score"] = round(probability,3)

        results.append(tutor)

    results = sorted(results, key=lambda x: x["match_score"], reverse=True)

    return results