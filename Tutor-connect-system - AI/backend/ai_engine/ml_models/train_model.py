from sklearn.ensemble import RandomForestClassifier
import joblib

from dataset_builder import build_training_data

def train():

    df = build_training_data()

    X = df.drop("chosen", axis=1)
    y = df["chosen"]

    model = RandomForestClassifier()

    model.fit(X, y)

    joblib.dump(model, "ai_engine/ml_models/tutor_model.pkl")

    print("Model trained successfully")


if __name__ == "__main__":
    train()