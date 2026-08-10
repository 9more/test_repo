from pathlib import Path

from sklearn.ensemble import ExtraTreesClassifier

from model_train import best_grid
import joblib
from data_split import data_split
BASE_PATH=Path(__file__).resolve().parent
MODEL_PATH=BASE_PATH.joinpath('models')
MODELS= ['ComplementNB()',
         'ExtraTreesClassifier()',
         'LinearSVC()',
         'LogisticRegression()',
         'SGDClassifier()',
         ]
test=data_split()['test']
for models in MODELS:
    print(MODEL_PATH)
    model= joblib.load(MODEL_PATH.joinpath(models))

    print(model)


