import pandas as pd

from services.model_registry import MODELS, THRESHOLDS
from services.encounter_service import get_encounter
from services.customer_service import get_customer_features

from schemas.churn import REQUIRED_FEATURES as CHURN_FEATURES
from schemas.readmission import REQUIRED_FEATURES as READMISSION_FEATURES

FEATURES = {"churn": CHURN_FEATURES, "readmission": READMISSION_FEATURES}


def predict(model_name, features=None, encounter_id=None, customer_id=None):
    def predict(model_name, features=None, encounter_id=None, customer_id=None):

        print(">>> PREDICT SERVICE CALLED <<<")

        if model_name not in MODELS:
            raise ValueError(f"Unknown model: {model_name}")

    if encounter_id is not None:

        features = get_encounter(encounter_id)

        if features is None:
            raise ValueError(f"Encounter {encounter_id} not found")

        print("FEATURE KEYS:")
        print(list(features.keys()))

        print("REQUIRED FEATURES:")
        print(FEATURES[model_name])

    elif customer_id is not None:

        features = get_customer_features(customer_id)

        if features is None:
            raise ValueError(f"No feature record found " f"for customer {customer_id}")

    if features is None:
        raise ValueError("No features provided")

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

        from services.prediction_database import save_prediction

        prediction_id = save_prediction(
            encounter_id=encounter_id,
            model_name=model_name,
            model_version="v1",
            probability=probability,
            threshold=threshold,
            prediction=prediction,
        )

    return {
        "model": model_name,
        "prediction": prediction,
        "probability": float(probability),
        "threshold": float(threshold),
        "prediction_id": prediction_id,
    }
