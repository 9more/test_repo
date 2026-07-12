import joblib
from class_files import Main
import spacy

def prediction(text):
    nlp = spacy.load('en_core_web_sm')
    def lemma(text):    
        doc = nlp(text)
        tok = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
        return ' '.join(tok).lower().strip()
    text=lemma(text)
    with open('saved_model.pkl', 'rb') as model:
        model=joblib.load(model)
        if model.predict([text])==1:
            print('Spam')
        else:
            print('Not Spam')

string= r"""Hello Micah,We have received your application for the Data Analytics Specialist position. 
Thank you for your interest. We'll be in touch once we've been able to review your application.
In the meantime, why not learn more about us
At BT we believe in empowering our people to thrive and make a real impact."""

prediction(string)
print(model.best_estimator_)