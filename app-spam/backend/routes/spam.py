from flask import Blueprint
from flask import jsonify
from flask import request

from model import classifier
from utils.validation import validate_message

predict_bp = Blueprint("predict", __name__)


@predict_bp.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    message = data["message"]

    if not validate_message(message):

        return jsonify({
            "error": "Invalid message."
        }), 400

    result = classifier.predict(message)

    LABEL_MAP = {
        0: "NOT SPAM",
        1: "SPAM"
    }

    result["prediction"] = LABEL_MAP[
        int(result["prediction"])
    ]

    return jsonify(result)