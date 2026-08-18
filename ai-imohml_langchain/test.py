import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("HF_TOKEN")
print(api_key)