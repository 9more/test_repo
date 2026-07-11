import pickle

MODEL_PATH = "trained_model.pkl"


class SpamClassifier:

    def __init__(self):
        with open(MODEL_PATH, "rb") as file:
            self.model = pickle.load(file)

    def predict(self, message):

        prediction = self.model.predict([message])[0]

        probability = self.model.predict_proba([message])[0]

        confidence = max(probability)

        label = "Spam" if prediction == 1 else "Not Spam"

        return {
            "prediction": label,
            "confidence": round(confidence * 100, 2)
        }


classifier = SpamClassifier()