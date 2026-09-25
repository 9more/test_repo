import requests

url = "http://127.0.0.1:5001/predict"


data = {"model": "readmission", "encounter_id": 1}


response = requests.post(url, json=data)


print("Status code:", response.status_code)

print("Response:")

print(response.json())
