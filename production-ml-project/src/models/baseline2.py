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

selected_features = [
    "eqpdays",
    "months",
    "change_mou",
    "totmrc_Mean",
    "mou_Mean",
    "avgqty",
    "asl_flag",
    "mou_cvce_Mean",
    "change_rev",
    "hnd_price",
    "mou_peav_Mean",
    "avg3mou",
    "comp_vce_Mean",
    "complete_Mean",
    "avgrev",
    "uniqsubs",
    "mou_opkv_Mean",
    "crclscod",
    "refurb_new",
    "totcalls",
]

X_reduced = df[selected_features]
y = df["churn"]
numeric_features_reduced = X_reduced.select_dtypes(include="number").columns.tolist()

categorical_features_reduced = X_reduced.select_dtypes(
    include=["object", "string"]
).columns.tolist()

numeric_pipeline_reduced = Pipeline([("imputer", SimpleImputer(strategy="median"))])

categorical_pipeline_reduced = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]
)

preprocessor_reduced = ColumnTransformer(
    [
        ("numeric", numeric_pipeline_reduced, numeric_features_reduced),
        ("categorical", categorical_pipeline_reduced, categorical_features_reduced),
    ]
)

reduced_model = Pipeline(
    [
        ("preprocessor", preprocessor_reduced),
        (
            "classifier",
            RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
        ),
    ]
)

X_train_reduced, X_test_reduced, y_train, y_test = train_test_split(
    X_reduced, y, test_size=0.2, random_state=42, stratify=y
)

reduced_model.fit(X_train_reduced, y_train)
y_prob_reduced = reduced_model.predict_proba(X_test_reduced)[:, 1]

reduced_auc = roc_auc_score(y_test, y_prob_reduced)

print("Reduced model ROC-AUC:", reduced_auc)
