from flask import Blueprint, jsonify, request
from services.prediction_history_service import get_prediction_history

history_bp = Blueprint("history", __name__)


@history_bp.route("/predictions/history", methods=["GET"])
def prediction_history():
    try:
        limit = request.args.get("limit", default=5, type=int)

        if limit is None or limit < 1 or limit > 7:
            return jsonify({"error": "Limit must be between 1 and 7."}), 400

        history = get_prediction_history(limit=limit)

        return jsonify({"count": len(history), "predictions": history}), 200

    except Exception as error:
        print("Prediction history error:", error)
        return jsonify({"error": "Unable to retrieve prediction history."}), 500
