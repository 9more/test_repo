print('hello')

import pickle
with open('models/insurance_model.pkl','rb') as f:
    model= pickle.load(f)
    print((model))
