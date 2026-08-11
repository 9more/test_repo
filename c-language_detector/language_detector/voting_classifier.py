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

def voting_class():
    voting= VotingClassifier(estimators=[('sgd', SGD),
                                     ('EXTR', EXTR),
                                     ('cbn', CBN),
                                     'lsvc',LSVC,
                                     ('LGR', LGR)],
                         voting='hard',
                         n_jobs=-1)

    voting.fit(train[0],train[1])
    voting.score(test[0],test[1])
    joblib.dump(voting, MODELS_DIR/'voting')

