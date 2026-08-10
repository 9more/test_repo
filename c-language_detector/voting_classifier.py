from sklearn.ensemble import VotingClassifier
from pathlib import Path
from data_split import data_split
import joblib

train=data_split()['train']
test=data_split()['test']

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"
SGD= joblib.load(MODELS_DIR/'SGDClassifier()')
EXTR= joblib.load(MODELS_DIR/'ExtraTreesClassifier()')
CBN= joblib.load(MODELS_DIR/'ComplementNB()')
LSVC= joblib.load(MODELS_DIR/'LinearSVC()')
LGR= joblib.load(MODELS_DIR / 'LogisticRegression()')

MODELS= ['ComplementNB()',
         'ExtraTreesClassifier()',
         'LinearSVC()',
         'LogisticRegression()',
         'SGDClassifier()',
         ]
estimators=[]
for model in MODELS:
    estimators.append((model[:4], joblib.load(MODELS_DIR/model)))


voting= VotingClassifier(estimators=estimators,
                         voting='hard',
                         n_jobs=-1)

voting.fit(train[0]['Text'],train[1])
print(voting.score(test[0]['Text'],test[1]))
print(voting.predict(['today is a beautiful day']))
