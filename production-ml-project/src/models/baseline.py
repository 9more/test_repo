import pandas as pd

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.inspection import permutation_importance
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
)

DATA_PATH = Path("data/raw/telecom_customer.csv")

df = pd.read_csv(DATA_PATH)

X = df.drop(columns=["churn", "Customer_ID"])
y = df["churn"]

numeric_features = X.select_dtypes(include="number").columns.tolist()

categorical_features = X.select_dtypes(include=["object", "string"]).columns.tolist()

print("Numerical features:", len(numeric_features))
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

model = Pipeline(
    [
        ("preprocessor", preprocessor),
        (
            "classifier",
            RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
        ),
    ]
)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model.fit(X_train, y_train)

print("Model training complete.")

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("\nModel Performance")
print("-----------------")

print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1       :", f1_score(y_test, y_pred))
print("ROC-AUC  :", roc_auc_score(y_test, y_prob))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

importances = model.named_steps["classifier"].feature_importances_

feature_names = model.named_steps["preprocessor"].get_feature_names_out()

importance_df = pd.DataFrame({"feature": feature_names, "importance": importances})

importance_df = importance_df.sort_values("importance", ascending=False)

print("\nTop 30 features:")
print(importance_df.head(30))

feature_corr = X[numeric_features].corr()

print("\nHighly correlated feature pairs:")

for i in range(len(feature_corr.columns)):
    for j in range(i):
        correlation = feature_corr.iloc[i, j]

        if abs(correlation) > 0.90:
            print(
                feature_corr.columns[i],
                "<->",
                feature_corr.columns[j],
                ":",
                round(correlation, 3),
            )
print(df[["totmou", "adjmou", "totcalls", "adjqty"]].head(10))

perm_importance = permutation_importance(
    model, X_test, y_test, scoring="roc_auc", n_repeats=5, random_state=42, n_jobs=-1
)

permutation_df = pd.DataFrame(
    {
        "feature": X_test.columns,
        "importance_mean": perm_importance.importances_mean,
        "importance_std": perm_importance.importances_std,
    }
)

permutation_df = permutation_df.sort_values("importance_mean", ascending=False)

print("\nPermutation importance:")
print(permutation_df.head(30))
