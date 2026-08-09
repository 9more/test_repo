from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.naive_bayes import ComplementNB
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import joblib
from data_split import data_split

train=data_split()['train']

tf=TfidfVectorizer(ngram_range = (2, 3),
                   max_df=70000, sublinear_tf=True)

models=[SGDClassifier(),
        ComplementNB(),
        LinearSVC(),
        ExtraTreesClassifier(),
        LogisticRegression()]

params=[{
        'loss':['log_loss', 'hinge'],
         'penalty':['l2','l1'],
         'alpha':[1e-3, 1e-5],
         'max_iter':[1000],
         'class_weight':['balanced']
        },

        {
            'alpha': [.5,1],
            'normalize': [True, False]
        },
        {
            'C':[.1, .5, 1],
            'max_iter':[2000],
            'class_weight':['balanced'],
        },
       {
           'n_estimators' : [200],
           'max_depth':[10, 50, 100],
           'min_samples_split':[10, 20],
           'class_weight': ['balanced'],

       },
        {
           'penalty':['l2','l1'],
           'C': [0.5, 1, 10],
           'solver':['saga'],
           'max_iter':[1000],
           'class_weight':['balanced'],
        }
]

def best_grid():
    best_models = {}
    best_scores = {}
    num=0
    for _ in zip(models, params):
        mum=+1
        pipe=Pipeline([('transformer',tf), ('model',_[0]) ])
        grid_num = GridSearchCV(pipe, param_grid= _[1], cv=5,
                                n_jobs=-1,
                               refit = True,
                               scoring='f1')
        grid_num.fit(train[0],train[1])
        best_models.setdefault(str(_[0]),grid_num.best_estimator_)
        joblib.dump(grid_num.best_estimator_, 'models/'+str(_[0]))
        best_scores.setdefault(str(_[0]),grid_num.best_score_)

    return best_models ,best_scores