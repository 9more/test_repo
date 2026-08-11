from pathlib import Path

from sklearn.ensemble import ExtraTreesClassifier

from model_train import best_grid
import joblib
from data_split import data_split
BASE_PATH=Path(__file__).parent.resolve().parent
MODEL_PATH=BASE_PATH.joinpath('c-language_detector' 'models')
MODELS= ['ComplementNB()',
         'ExtraTreesClassifier()',
         'LinearSVC()',
         'LogisticRegression()',
         'SGDClassifier()',
         ]
print(MODEL_PATH)

print(BASE_PATH)


