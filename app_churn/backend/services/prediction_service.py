import pandas as pd
from services.model_registry import MODELS, THRESHOLDS
from schemas.churn import REQUIRED_FEATURES as CHURN_FEATURES
from schemas.readmission import REQUIRED_FEATURES as READMISSION_FEATURES

FEATURES = {"churn": CHURN_FEATURES, "readmission": READMISSION_FEATURES}


def predict(model_name, features):

    if model_name not in MODELS:
        raise ValueError(f"Unknown model: {model_name}")

    required_features = FEATURES[model_name]

    missing_features = [
        feature for feature in required_features if feature not in features
    ]

    if missing_features:
        raise ValueError(f"Missing features: {missing_features}")

    model = MODELS[model_name]

    input_data = pd.DataFrame([features])

    probability = model.predict_proba(input_data)[0][1]

    threshold = THRESHOLDS.get(model_name, 0.5)

    prediction = int(probability >= threshold)

    return {
        "model": model_name,
        "prediction": prediction,
        "probability": float(probability),
        "threshold": float(threshold),
    }
