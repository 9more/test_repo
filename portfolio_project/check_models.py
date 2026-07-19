from pathlib import Path
import joblib

MODELS_DIR = Path("models")

model_files = [
    "spam_model.joblib",
    "sentiment_model.joblib",
    "insurance_cost_model.joblib",
    "insurance_risk_model.joblib",
]

for filename in model_files:
    path = MODELS_DIR / filename
    print(f"\n{'=' * 60}")

    if not path.exists():
        print(f"Missing: {path}")
        continue

    model = joblib.load(path)

    print(f"Loaded: {filename}")
    print(f"Type: {type(model).__name__}")

    if hasattr(model, "named_steps"):
        print(f"Pipeline steps: {list(model.named_steps.keys())}")

    if hasattr(model, "feature_names_in_"):
        print(f"Input features: {list(model.feature_names_in_)}")

    if hasattr(model, "classes_"):
        print(f"Classes: {list(model.classes_)}")

    if hasattr(model, "best_estimator_"):
        print("Note: this is a GridSearchCV object; save best_estimator_ for deployment.")