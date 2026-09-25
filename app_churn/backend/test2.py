import requests

url = "http://127.0.0.1:5001/patients/1/encounters"


data = {
    "admission_type_id": 1,
    "discharge_disposition_id": 1,
    "admission_source_id": 7,
    "time_in_hospital": 5,
    "num_lab_procedures": 45,
    "num_procedures": 1,
    "num_medications": 15,
    "number_outpatient": 0,
    "number_emergency": 1,
    "number_inpatient": 2,
    "number_diagnoses": 8,
    "weight": None,
    "payer_code": "MC",
    "medical_specialty": "InternalMedicine",
    "diag_1": "428",
    "diag_2": "250.01",
    "diag_3": "401",
    "max_glu_serum": "None",
    "A1Cresult": ">8",
    "metformin": "Steady",
    "repaglinide": "No",
    "nateglinide": "No",
    "chlorpropamide": "No",
    "glimepiride": "No",
    "acetohexamide": "No",
    "glipizide": "No",
    "glyburide": "No",
    "tolbutamide": "No",
    "pioglitazone": "No",
    "rosiglitazone": "No",
    "acarbose": "No",
    "miglitol": "No",
    "troglitazone": "No",
    "tolazamide": "No",
    "examide": "No",
    "citoglipton": "No",
    "insulin": "Up",
    "glyburide-metformin": "No",
    "glipizide-metformin": "No",
    "glimepiride-pioglitazone": "No",
    "metformin-rosiglitazone": "No",
    "metformin-pioglitazone": "No",
    "change": "Ch",
    "diabetesMed": "Yes",
}


response = requests.post(url, json=data)


print("Status code:", response.status_code)
print("Response:")
print(response.json())
