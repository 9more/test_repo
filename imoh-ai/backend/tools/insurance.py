from tools.insurance_predictor import run as predict_charge
from tools.insurance_risk import run as predict_risk


def run(data):

    charge = predict_charge(data)

    risk = predict_risk(data)

    return {
    "tool": "insurance",
    "status": "success",
    "charge": round(float(charge["prediction"]), 2),
    "risk": risk["prediction"],
    "currency": "GBP",
}