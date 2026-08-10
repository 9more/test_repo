import os
import pandas as pd
import kagglehub
from dotenv import load_dotenv

load_dotenv(verbose=True)
AUTHENTICATION_KEY= os.getenv("AUTHENTICATION_KEY")
path = kagglehub.dataset_download("basilb2s/language-detection")
print("Path to dataset files:", path)

def data():
    return pd.read_csv(f'{path}/Language Detection.csv')


