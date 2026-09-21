import joblib

churn_model = joblib.load("backend/models/churn/churn_model.joblib")

readmission_model = joblib.load("backend/models/readmission/readmission_model.joblib")

threshold = joblib.load("backend/models/readmission/threshold.joblib")

print("Churn model:", type(churn_model))
print("Readmission model:", type(readmission_model))
print("Threshold:", threshold)
print(churn_model)
print(readmission_model)
