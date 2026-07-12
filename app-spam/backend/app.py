from flask import Flask, request, jsonify
from flask_cors import CORS

from src.predictor import predict_email


app = Flask(__name__)

# Allow React frontend to communicate with Flask backend
CORS(app)


@app.route("/", methods=["GET"])
def home():

    return jsonify(
        {
            "message": "Spam Detection API is running"
        }
    )


@app.route("/health", methods=["GET"])
def health():

    return jsonify(
        {
            "status": "healthy"
        }
    )


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        if not data:

            return jsonify(
                {
                    "error": "No JSON data received"
                }
            ), 400


        email = data.get("message")


        if not email:

            return jsonify(
                {
                    "error": "No email message provided"
                }
            ), 400


        result = predict_email(email)


        return jsonify(result), 200


    except Exception as e:

        return jsonify(
            {
                "error": str(e)
            }
        ), 500



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )





