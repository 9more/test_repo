from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent


MODELS = {
    "churn": joblib.load(BASE_DIR / "models/churn/churn_model.joblib"),
    "readmission": joblib.load(
        BASE_DIR / "models/readmission/readmission_model.joblib"
    ),
}


THRESHOLDS = {
    "readmission": joblib.load(BASE_DIR / "models/readmission/threshold.joblib")
}
