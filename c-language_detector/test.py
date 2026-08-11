import joblib
from pathlib import Path

BASE_PATH=Path(__file__).parent.resolve().parent
MODEL_PATH=BASE_PATH.joinpath('c-language_detector')
MODELS= ['ComplementNB()',
         'ExtraTreesClassifier()',
         'LinearSVC()',
         'LogisticRegression()',
         'SGDClassifier()',
         ]
print(MODEL_PATH)

print(BASE_PATH)

model =joblib.load('models/voting.joblib')
print(model.predict(['Main kitaab padhta hoon']))


