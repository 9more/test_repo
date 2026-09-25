from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
from data.fetch import df

BASE_DIR = Path(__file__).resolve().parent
HOME_DIR = Path.home()
DESTINATION_DIR = (
    HOME_DIR / "test_repo/app_churn" / "backend" / "models" / "readmission"
)

df["target"] = (df["readmitted"] == "<30").astype(int)
X = df.drop(columns=["readmitted", "target", "encounter_id", "patient_nbr"])

y = df["target"]

print("X shape:", X.shape)
print("y shape:", y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print("Training:", y_train.value_counts(normalize=True))
print("Testing:", y_test.value_counts(normalize=True))
numeric_features = X.select_dtypes(include="number").columns.tolist()

categorical_features = X.select_dtypes(include=["object", "string"]).columns.tolist()

print("Numeric features:", len(numeric_features))
print("Categorical features:", len(categorical_features))

numeric_pipeline = Pipeline([("imputer", SimpleImputer(strategy="median"))])

categorical_pipeline = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]
)

preprocessor = ColumnTransformer(
    [
        ("numeric", numeric_pipeline, numeric_features),
        ("categorical", categorical_pipeline, categorical_features),
    ]
)

logistic_model = Pipeline(
    [
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ]
)

rf_model = Pipeline(
    [
        ("preprocessor", preprocessor),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=300, random_state=42, n_jobs=-1, class_weight="balanced"
            ),
        ),
    ]
)

xgb_model = Pipeline(
    [
        ("preprocessor", preprocessor),
        (
            "classifier",
            XGBClassifier(
                n_estimators=300,
                max_depth=6,
                learning_rate=0.05,
                subsample=0.8,
                colsample_bytree=0.8,
                random_state=42,
                eval_metric="logloss",
                n_jobs=-1,
            ),
        ),
    ]
)

logistic_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)
xgb_model.fit(X_train, y_train)

models = {
    "Logistic Regression": logistic_model,
    "Random Forest": rf_model,
    "XGBoost": xgb_model,
}

for name, model in models.items():
    y_prob = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_prob)
    print(f"{name}: {auc:.4f}")


joblib.dump(xgb_model, DESTINATION_DIR / "readmission_model.joblib")

print(f"Best threshold saved to, {DESTINATION_DIR}")
print(xgb_model)
