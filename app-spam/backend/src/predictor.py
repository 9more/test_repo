import pickle
from pathlib import Path
import spacy 


MODEL_PATH = Path(__file__).parent.parent / "model" / "spam_model.pkl"


with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)



def preprocess_text(text):

    nlp = spacy.load('en_core_web_sm')
    def lemma(text):    
        doc = nlp(text)
        tok = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
        return ' '.join(tok).lower().strip()# Put your existing preprocessing here
    

    processed_text = text.lower()

    return processed_text



def predict_email(email):

    processed_email = preprocess_text(email)


    prediction = model.predict(
        [processed_email]
    )


    probability = None

    if hasattr(model, "predict_proba"):

        probability = (
            model.predict_proba([processed_email])
            .max()
        )


    result = {

        "prediction":
            "Spam"
            if prediction[0] == 1
            else "Not Spam",

        "confidence":
            round(probability * 100, 2)
            if probability
            else None

    }


    return result
