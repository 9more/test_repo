import spacy
nlp = spacy.load('en_core_web_sm')

def lemma(text):    
    doc = nlp(text)
    tok = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
    return ' '.join(tok).lower().strip()

string= """Hello Micah,We have received your application for the Data Analytics Specialist position. 
Thank you for your interest. We'll be in touch once we've been able to review your application.
In the meantime, why not learn more about us
At BT we believe in empowering our people to thrive and make a real impact."""

print(lemma(string))
    