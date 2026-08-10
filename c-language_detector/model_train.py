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

train = data_split()['train']

tf = TfidfVectorizer(
    analyzer='char',
    ngram_range=(2, 5),
    sublinear_tf=True,
    min_df=1
)

models = [SGDClassifier(),
          ComplementNB(),
          LinearSVC(),
          ExtraTreesClassifier(),
          LogisticRegression()]

params = [{
    'models__loss': ['log_loss', 'hinge'],
    'models__penalty': ['l2', 'l1'],
    'models__alpha': [1e-3, 1e-5],
    'models__max_iter': [1000],
    'models__class_weight': ['balanced']
},

    {
        'models__alpha': [0.5, 1]
    },
    {
        'models__C': [0.1, 0.5, 1],
        'models__max_iter': [2000],
        'models__class_weight': ['balanced']
    },
    {
        'models__n_estimators': [200],
        'models__max_depth': [10, 50, 100],
        'models__min_samples_split': [10, 20],
        'models__class_weight': ['balanced']
    },

    {
        'models__penalty': ['l2', 'l1'],
        'models__C': [0.5, 1, 10],
        'models__solver': ['saga'],
        'models__max_iter': [1000],
        'models__class_weight': ['balanced']
    }
]


def best_grid():
    best_models = {}
    best_scores = {}
    for model, param in zip(models, params):
        pipe = Pipeline([
            ('transformer', tf),
            ('models', model)
        ])
        grid_num = GridSearchCV(
            estimator=pipe,
            param_grid=param,
            cv=5,
            n_jobs=-1,
            refit=True,
            scoring='f1_macro',
            error_score='raise'
        )
        print("X type:", type(train[0]))
        print("X shape:", train[0].shape)
        print("y type:", type(train[1]))
        print("y shape:", train[1].shape)
        print(train[1].head())
        grid_num.fit(train[0]['Text'], train[1])
        best_models[str(model)] = grid_num.best_estimator_
        best_scores[str(model)] = grid_num.best_score_
        joblib.dump(grid_num.best_estimator_, 'models/' + str(model))
    return best_models, best_scores



