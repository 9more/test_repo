import pandas as pd

from services.model_registry import MODELS, THRESHOLDS

from schemas.churn import REQUIRED_FEATURES as CHURN_FEATURES
from schemas.readmission import REQUIRED_FEATURES as READMISSION_FEATURES

from services.encounter_service import get_encounter
from services.prediction_database import save_prediction

FEATURES = {"churn": CHURN_FEATURES, "readmission": READMISSION_FEATURES}


def predict(model_name, features=None, encounter_id=None):

    if model_name not in MODELS:
        raise ValueError(f"Unknown model: {model_name}")

    if encounter_id is not None:

        features = get_encounter(encounter_id)

        if features is None:
            raise ValueError(f"Encounter {encounter_id} not found")

    if features is None:
        raise ValueError("Features or encounter_id are required")

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

    prediction_id = None

    if encounter_id is not None:

        prediction_id = save_prediction(
            encounter_id=encounter_id,
            model_name=model_name,
            model_version="v1",
            probability=float(probability),
            threshold=float(threshold),
            prediction=prediction,
        )

    return {
        "prediction_id": prediction_id,
        "model": model_name,
        "prediction": prediction,
        "probability": float(probability),
        "threshold": float(threshold),
    }
