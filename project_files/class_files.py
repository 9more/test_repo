"""The main class that supplies other files"""
import kagglehub
import os
import joblib
import pandas as pd
import numpy as np
import spacy
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics import f1_score
# Do not call interactive login at import time; call externally if needed

class Main:
    def get_data():
        # Download latest version
        path = kagglehub.dataset_download("jackksoncsie/spam-email-dataset")
        path=path.replace('.cache', 'Documents')
        return path

    def load(path):
        df= pd.read_csv(f'{path}/emails.csv')
        return df

    def graph():
        pass

    def extract(df):
        nlp = spacy.load('en_core_web_sm')

        def lemma(text):
            # Ensure text is treated as a single string
            doc = nlp(str(text))
            tok = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
            return ' '.join(tok).strip()

        df['text_xtract'] = df['text'].str.lower().apply(lemma)
        return df

    def model_train(df):
        Xtrain, Xtest, ytrain, ytest=train_test_split(
                            df['text_xtract'].values,df['spam'].values,
                            test_size=.1,
                            random_state=42,
                            shuffle=True)
        pipe=Pipeline([('transformer',TfidfVectorizer()),
               ('model', LinearSVC())
              ]
             )
        params = [
            {
                'model': [LinearSVC()],
                'model__C': np.linspace(0.5, 2, 6),
                'model__class_weight': [{0: 1, 1: v} for v in range(1, 6)]
            },
            {
                'model': [LogisticRegression(max_iter=1000)],
                'model__C': np.linspace(0.5, 2, 6),
                'model__class_weight': [{0: 1, 1: v} for v in range(1, 6)]
            }
            ]
        grid= GridSearchCV(pipe,
                        param_grid=params,
                        cv=5,
                        #scoring='f1',
                        refit=True,
                        verbose=10)
        model= grid.fit(Xtrain, ytrain)
        return model, Xtest, ytest
    

    def model_eval(model, Xtest, ytest):
        preds = model.best_estimator_.predict(Xtest)
        return f1_score(ytest, preds)
    
    def model_dump(model, file):
        joblib.dump(model, f'{file}.pkl')
    
    



