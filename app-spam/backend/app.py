from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from utils.preprocessing import preprocess_text
from model import sentiment_classifier

app = Flask(__name__)

CORS(
    app,
    resources={
        r"/*": {
            "origins": "*"
        }
    }
)

@app.after_request
def after_request(response):

    response.headers.add(
        "Access-Control-Allow-Origin",
        "*"
    )

    response.headers.add(
        "Access-Control-Allow-Headers",
        "Content-Type,Authorization"
    )

    response.headers.add(
        "Access-Control-Allow-Methods",
        "GET,PUT,POST,DELETE,OPTIONS"
    )

    return response

with open("models/spam_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():

    return {
        "status": "running",
        "message": "Portfolio API"
    }


@app.route("/predict/spam", methods=["POST"])
def predict_spam():

    data = request.get_json()

    message = data.get("message", "")

    clean_text = preprocess_text(message)

    prediction = model.predict([clean_text])[0]

    LABEL_MAP = {
        0: "Not Spam",
        1: "Spam"
    }

    return jsonify({
        "prediction": LABEL_MAP[int(prediction)],
        "confidence": 100
    })

@app.route("/predict/sentiment", methods=["POST"])
def predict_sentiment():

    data = request.get_json()

    text = data.get("text", "")

    result = sentiment_classifier.predict(text)

    return jsonify(result)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )