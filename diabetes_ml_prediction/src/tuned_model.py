from sklearn.model_selection import RandomizedSearchCV
from train import xgb_model, X_train, y_train, X_test, y_test
from sklearn.metrics import roc_auc_score

param_grid = {
    "classifier__n_estimators": [200, 300, 500],
    "classifier__max_depth": [3, 5, 7],
    "classifier__learning_rate": [0.03, 0.05, 0.1],
    "classifier__subsample": [0.8, 1.0],
    "classifier__colsample_bytree": [0.8, 1.0],
}

xgb_search = RandomizedSearchCV(
    estimator=xgb_model,
    param_distributions=param_grid,
    n_iter=15,
    scoring="roc_auc",
    cv=3,
    random_state=42,
    n_jobs=-1,
)

xgb_search.fit(X_train, y_train)

print("Best ROC-AUC:", xgb_search.best_score_)
print("Best parameters:")
print(xgb_search.best_params_)

best_xgb = xgb_search.best_estimator_

y_prob = best_xgb.predict_proba(X_test)[:, 1]

test_auc = roc_auc_score(y_test, y_prob)

print("Test ROC-AUC:", test_auc)
