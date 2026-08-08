from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"


class ModelRegistry:
    """
    Central registry for all production ML models.
    """

    def __init__(self):
        self._models = {}

    def load(self, name: str, filename: str):
        path = MODELS_DIR / filename

        if not path.exists():
            raise FileNotFoundError(
                f"Model '{filename}' not found in {MODELS_DIR}"
            )

        self._models[name] = joblib.load(path)

    def get(self, name: str):
        return self._models[name]


registry = ModelRegistry()

# Load production models
registry.load("spam", "spam_model.joblib")
registry.load("sentiment", "sentiment_model.joblib")
registry.load("insurance_predictor","insurance_predictor.pkl")
registry.load( "insurance_risk","insurance_risk.pkl")
#registry.load("diabetes","diabetes.pkl")
#registry.load( "language","language_detector.joblib")