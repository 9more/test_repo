from flask import Blueprint, request, jsonify

from services.patient_service import create_patient

patients_bp = Blueprint("patients", __name__)


@patients_bp.route("/patients", methods=["POST"])
def register_patient():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    gender = data.get("gender")
    race = data.get("race")
    age = data.get("age")

    patient_id = create_patient(gender, race, age)

    return (
        jsonify(
            {"patient_id": patient_id, "message": "Patient registered successfully"}
        ),
        201,
    )
