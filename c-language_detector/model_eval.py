import joblib
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
<<<<<<< HEAD
from data_split import data_split
from pathlib import Path
import pandas as pd

test=data_split()['test']

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"

MODELS= ['ComplementNB()',
         'ExtraTreesClassifier()',
         'LinearSVC()',
         'LogisticRegression()',
         'SGDClassifier()',
         'voting.joblib',
         ]
for models in MODELS:
    model = joblib.load(MODELS_DIR / models)
    y_pred = model.predict(test[0]['Text'])
    cls_report = classification_report(test[1],y_pred,output_dict=True)
    df = pd.DataFrame(cls_report).transpose()
    print('\n\n')
    print(f'score for {models}')
    print('++++++++++++++++++++++++++++++++++')

    print('++++++++++++++++++++++++++++++++++')
    print(df)
=======
from model_train import best_grid

>>>>>>> frontend
