from joblib import load

model = load("models/sentiment_model.joblib")

print(model.predict(["the product was really terrible"]))