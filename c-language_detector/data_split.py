from get_data import data
from sklearn.model_selection import train_test_split


df = data()
def data_split():

    Xtrain, Xtest, ytrain, ytest=train_test_split(
        df.iloc[:,:-1],df.iloc[:,-1],
         test_size=0.2,random_state=0,stratify=df.iloc[:,-1],
         shuffle=True)

    return {'train':[Xtrain, ytrain] ,'test': [Xtest, ytest]}