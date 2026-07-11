from flask import Blueprint
from flask import jsonify
from flask import request

from model import classifier
from utils.validator import validate_message

predict_bp = Blueprint("predict", __name__)


@predict_bp.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if "message" not in data:

        return jsonify({
            "error": "Message not provided."
        }), 400

    message = data["message"]

    if not validate_message(message):

        return jsonify({
            "error": "Invalid message."
        }), 400

    result = classifier.predict(message)

    return jsonify(result)