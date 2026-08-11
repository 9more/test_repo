from sklearn.ensemble import VotingClassifier
from pathlib import Path
from data_split import data_split
import joblib

train=data_split()['train']
test=data_split()['test']

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"

MODELS= ['ComplementNB()',
         'ExtraTreesClassifier()',
         'LinearSVC()',
         'LogisticRegression()',
         'SGDClassifier()',
         ]
estimators=[(model[:4], joblib.load(MODELS_DIR/model)) for model in MODELS]


voting= VotingClassifier(estimators=estimators,
                         voting='hard',
                         n_jobs=-1)

voting.fit(train[0]['Text'],train[1])
print(voting.score(test[0]['Text'],test[1]))
joblib.dump(voting, Path.joinpath(MODELS_DIR,'voting.joblib'))
print(voting.predict(['today is a beautiful day']))
