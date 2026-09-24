from flask import Blueprint, request, jsonify

from services.prediction_service import predict

prediction_bp = Blueprint("prediction", __name__)


@prediction_bp.route("/predict", methods=["POST"])
def prediction():

    try:

        data = request.get_json()

        if not data:
            return jsonify({"error": "Request body is required"}), 400

        model_name = data.get("model")
        features = data.get("features")

        if not model_name:
            return jsonify({"error": "Model name is required"}), 400

        if not features:
            return jsonify({"error": "Features are required"}), 400

        result = predict(model_name, features)

        return jsonify(result)

    except ValueError as error:

        return jsonify({"error": str(error)}), 400

    except Exception as error:

        print("Prediction error:", error)

        return jsonify({"error": str(error)}), 500
