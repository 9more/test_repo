import joblib

MODEL = joblib.load("models/spam_model.joblib")


def run(payload: dict) -> dict:
    """
    Email Threat Detection
    """

    message = payload["message"]

    prediction = MODEL.predict([message])[0]

    return {
        "tool": "spam",
        "status": "success",
        "prediction": prediction,
    }