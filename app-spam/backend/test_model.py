print('hello')

import pickle
with open('models/insurance_risk_model.pkl','rb') as f:
    model= pickle.load(f)
    print((model.best_estimator_))

