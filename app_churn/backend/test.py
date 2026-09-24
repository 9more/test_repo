import joblib

threshold = 0.15

churn_model = joblib.load("backend/models/churn/churn_model.joblib")
joblib.dump(threshold, "backend/models/churn/threshold.joblib")
thresh = joblib.load("backend/models/churn/threshold.joblib")


print("=" * 60)
print("printing readmission model:")
print(readmit)
print("=" * 60, "\n")

print("=" * 60)
print("printing threshold:")
print(thresh)
print("=" * 60, "\n")
