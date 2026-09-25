from flask import Blueprint, request, jsonify

from services.encounter_service import create_encounter

encounters_bp = Blueprint("encounters", __name__)


@encounters_bp.route("/patients/<int:patient_id>/encounters", methods=["POST"])
def register_encounter(patient_id):

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    try:

        encounter_id = create_encounter(patient_id, data)

        return (
            jsonify(
                {
                    "encounter_id": encounter_id,
                    "patient_id": patient_id,
                    "message": "Encounter registered successfully",
                }
            ),
            201,
        )

    except KeyError as error:

        return jsonify({"error": f"Missing feature: {error.args[0]}"}), 400
