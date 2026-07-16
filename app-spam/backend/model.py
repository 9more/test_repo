from pathlib import Path
import pickle

from utils.preprocessing import preprocess_text

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "spam_model.pkl"


class SpamClassifier:

    def __init__(self):

        with open(MODEL_PATH, "rb") as file:
            self.model = pickle.load(file)

    def predict(self, message):

        clean_text = preprocess_text(message)

        prediction = self.model.predict(
            [clean_text]
        )[0]

        label = (
            "Spam"
            if int(prediction) == 1
            else "Not Spam"
        )

        return {
            "prediction": label,
            "confidence": 100
        }


classifier = SpamClassifier()

#=======================================================================
#Sentiment Analysis Model
#=======================================================================

class SentimentClassifier:

    def __init__(self):

        with open(
            BASE_DIR / "models" / "sentiment_model.pkl",
            "rb"
        ) as file:

            self.model = pickle.load(file)

    def predict(self, text):

        clean_text = preprocess_text(text)

        prediction = self.model.predict(
            [clean_text]
        )[0]

        label = (
            "Positive Sentiment"
            if int(prediction) == 1
            else "Negative Sentiment"
        )

        return {
            "prediction": label,
            "confidence": 100
        }


sentiment_classifier = SentimentClassifier()



#==========================================================================================

# INSURANCXE ESTIMATOR

#=========================================================================================

class InsuranceEstimator:

    def __init__(self):

        with open(
            BASE_DIR / "models" / "insurance_model.pkl",
            "rb"
        ) as file:

            self.model = pickle.load(file)

    def predict(self, data):

        prediction = self.model.predict([data])[0]

        return {
            "estimatedCharge":
                round(float(prediction), 2)
        }


insurance_estimator = InsuranceEstimator()


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# INSURANCE ESTIMATOR
#==========================================================

import pickle
import pandas as pd

class InsuranceEstimator:

    def __init__(self):

        with open(
            "models/insurance_model.pkl",
            "rb"
        ) as f:

            self.model = pickle.load(f)

    def predict(self, data):

        X = pd.DataFrame([data])

        prediction = self.model.predict(X)[0]

        return {
            "estimatedCharge":
                round(float(prediction), 2)
        }


insurance_estimator = InsuranceEstimator()

#======================================================================
# INSURANCE RISK CLASSIFIER
#======================================================================

class InsuranceRiskClassifier:

    def __init__(self):

        with open(
            "models/insurance_risk_model.pkl",
            "rb"
        ) as f:

            self.model = pickle.load(f)

    def predict(self, data):

        X = pd.DataFrame([data])

        prediction = self.model.predict(X)[0]

        probability = float(
            max(
                self.model.predict_proba(X)[0]
            )
        )

        return {
            "prediction": prediction,
            "confidence": round(
                probability * 100,
                2
            )
        }
    
    
insurance_risk_classifier = InsuranceRiskClassifier()