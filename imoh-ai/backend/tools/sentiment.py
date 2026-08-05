from joblib import load

model = load("models/sentiment_model.joblib")


def run(data):

    text = data["message"]

    prediction = model.predict([text])[0]

    return {
        "tool": "sentiment",
        "status": "success",
        "prediction": prediction,
    }