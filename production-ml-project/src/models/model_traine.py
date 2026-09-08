from sklearn.model_selection import RandomizedSearchCV
from baseline import df
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

param_grid = {
    "classifier__n_estimators": [100, 200, 300],
    "classifier__max_depth": [None, 10, 20, 30],
    "classifier__min_samples_split": [2, 5, 10],
    "classifier__min_samples_leaf": [1, 2, 4],
    "classifier__max_features": ["sqrt", "log2"],
}

selected_features_v2 = [
    "eqpdays",
    "months",
    "change_mou",
    "totmrc_Mean",
    "mou_Mean",
    "avgqty",
    "asl_flag",
    "change_rev",
    "hnd_price",
    "mou_cvce_Mean",
    "avg3mou",
    "uniqsubs",
    "crclscod",
    "refurb_new",
    "totcalls",
]


X_reduced_v2 = df[selected_features_v2]
y = df["churn"]

numeric_features_v2 = X_reduced_v2.select_dtypes(include="number").columns.tolist()

categorical_features_v2 = X_reduced_v2.select_dtypes(
    include=["object", "string"]
).columns.tolist()

numeric_pipeline_v2 = Pipeline([("imputer", SimpleImputer(strategy="median"))])

categorical_pipeline_v2 = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]
)
preprocessor_v2 = ColumnTransformer(
    [
        ("numeric", numeric_pipeline_v2, numeric_features_v2),
        ("categorical", categorical_pipeline_v2, categorical_features_v2),
    ]
)

model_v2 = Pipeline(
    [("preprocessor", preprocessor_v2), ("classifier", RandomForestClassifier(...))]
)

search = RandomizedSearchCV(
    estimator=model_v2,
    param_distributions=param_grid,
    n_iter=15,
    scoring="roc_auc",
    cv=3,
    random_state=42,
    n_jobs=-1,
)

X_train_v2, X_test_v2, y_train, y_test = train_test_split(
    X_reduced_v2, y, test_size=0.2, random_state=42, stratify=y
)

search.fit(X_train_v2, y_train)

print("Best ROC-AUC:", search.best_score_)
print("Best parameters:", search.best_params_)

best_model = search.best_estimator_
y_prob_tuned = best_model.predict_proba(X_test_v2)[:, 1]

test_auc = roc_auc_score(y_test, y_prob_tuned)

print("Final Test ROC-AUC:", test_auc)

import joblib

joblib.dump(best_model, "..\\..\\churn_model.joblib")
