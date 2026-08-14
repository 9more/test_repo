from pathlib import Path

from sklearn.ensemble import ExtraTreesClassifier

from model_train import best_grid
import joblib
from data_split import data_split
BASE_PATH=Path(__file__).parent.resolve().parent
MODEL_PATH=BASE_PATH.joinpath('c-language_detector','models')
MODELS= ['ComplementNB()',
         'ExtraTreesClassifier()',
         'LinearSVC()',
         'LogisticRegression()',
         'SGDClassifier()',
         'voting.joblib'
         ]
print(MODEL_PATH)
print(BASE_PATH)
for model in MODELS:
    if model == 'voting.joblib':
        model = joblib.load(MODEL_PATH/model)
        print(type(model))
        print(model.classes_)
        print(model.named_estimators_)
        texts = [
            "Hello, how are you today?",
            "Bonjour, comment allez-vous?",
            "Hola, ¿cómo estás?",
            "Guten Morgen, wie geht es dir?",
        ]
        print(model.predict(texts))

