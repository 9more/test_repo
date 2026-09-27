from flask import Blueprint, request, jsonify

from services.customer_service import create_customer, create_customer_features

customers_bp = Blueprint("customers", __name__)


@customers_bp.route("/customers", methods=["POST"])
def register_customer():

    try:

        customer_id = create_customer()

        return (
            jsonify(
                {
                    "customer_id": customer_id,
                    "message": "Customer registered successfully",
                }
            ),
            201,
        )

    except Exception as error:

        print("Customer registration error:", error)

        return jsonify({"error": "Customer registration failed"}), 500


@customers_bp.route("/customers/<int:customer_id>/features", methods=["POST"])
def register_customer_features(customer_id):

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    try:

        feature_record_id = create_customer_features(customer_id, data)

        return (
            jsonify(
                {
                    "customer_id": customer_id,
                    "feature_record_id": feature_record_id,
                    "message": "Customer features registered successfully",
                }
            ),
            201,
        )

    except KeyError as error:

        return jsonify({"error": f"Missing feature: {error.args[0]}"}), 400

    except Exception as error:

        print("Customer feature error:", error)

        return jsonify({"error": "Customer feature registration failed"}), 500
