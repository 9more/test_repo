from flask import Blueprint, request, jsonify

from services.prediction_service import predict

prediction_bp = Blueprint("prediction", __name__)


@prediction_bp.route("/predict", methods=["POST"])
def prediction():

    data = request.get_json()

    model_name = data.get("model")
    features = data.get("features")

    result = predict(model_name, features)

    return jsonify(result)
