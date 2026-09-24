import requests

url = "http://127.0.0.1:5001/predict"

data = {
    "model": "churn",
    "features": {
        "eqpdays": 200,
        "months": 24,
        "change_mou": -50,
        "totmrc_Mean": 50,
        "mou_Mean": 300,
        "avgqty": 2,
        "asl_flag": "Y",
        "change_rev": -5,
        "hnd_price": 100,
        "mou_cvce_Mean": 250,
        "avg3mou": 300,
        "uniqsubs": 1,
        "crclscod": "A",
        "refurb_new": "N",
        "totcalls": 100,
    },
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response:")
print(response.content.decode("utf-8"))
print("Headers:")
print(response.headers)
print("JSON:")
print(response.json())
