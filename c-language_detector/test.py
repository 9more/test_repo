import joblib
from pathlib import Path

BASE_PATH=Path(__file__).parent.resolve().parent
<<<<<<< HEAD
MODEL_PATH=BASE_PATH.joinpath('c-language_detector')
=======
MODEL_PATH=BASE_PATH.joinpath('c-language_detector','models')
>>>>>>> frontend
MODELS= ['ComplementNB()',
         'ExtraTreesClassifier()',
         'LinearSVC()',
         'LogisticRegression()',
         'SGDClassifier()',
         'voting.joblib'
         ]
print(MODEL_PATH)
print(BASE_PATH)
<<<<<<< HEAD

model =joblib.load('models/voting.joblib')
print(model.predict(['Main kitaab padhta hoon']))

=======
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
>>>>>>> frontend

