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

        encounter_id = data.get("encounter_id")

        if not model_name:
            return jsonify({"error": "Model name is required"}), 400

        if features is None and encounter_id is None:
            return jsonify({"error": "Features or encounter_id are required"}), 400

        result = predict(
            model_name=model_name, features=features, encounter_id=encounter_id
        )

        return jsonify(result)

    except ValueError as error:

        return jsonify({"error": str(error)}), 400

    except Exception as error:

        print("Prediction error:", error)

        return jsonify({"error": str(error)}), 500
