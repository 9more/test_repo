import pandas as pd

from services.model_registry import MODELS, THRESHOLDS


def predict(model_name, features):

    if model_name not in MODELS:
        raise ValueError(f"Unknown model: {model_name}")

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
