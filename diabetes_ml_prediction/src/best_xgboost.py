from pathlib import Path
import joblib
from train import xgb_model, X_train, y_train, X_test, y_test
import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)

BASE_DIR = Path(__file__).resolve().parent
HOME_DIR = Path.home()
DESTINATION_DIR = HOME_DIR / "test_repo/app_churn/backend/models/readmission"

y_prob = xgb_model.predict_proba(X_test)[:, 1]

thresholds = np.arange(0.01, 0.51, 0.01)

results = []

for threshold in thresholds:
    y_pred = (y_prob >= threshold).astype(int)

    precision = precision_score(y_test, y_pred, zero_division=0)

    recall = recall_score(y_test, y_pred, zero_division=0)

    f1 = f1_score(y_test, y_pred, zero_division=0)

    results.append(
        {"threshold": threshold, "precision": precision, "recall": recall, "f1": f1}
    )

results_df = pd.DataFrame(results)

best_threshold = results_df.loc[results_df["f1"].idxmax()]

print(f"Best threshold saved to, {DESTINATION_DIR}")

print(best_threshold)
