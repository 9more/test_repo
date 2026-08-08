from model_registry import registry
    
import pandas as pd

from model_registry import registry


def run(data):

    df = pd.DataFrame(
        [
            {
                "age": data["age"],
                "sex": data["sex"],
                "bmi": data["bmi"],
                "children": data["children"],
                "smoker": data["smoker"],
                "region": data["region"],
            }
        ]
    )

    prediction = registry.get(
        "insurance_predictor"
    ).predict(df)[0]

    return {
        "tool": "insurance_predictor",
        "status": "success",
        "prediction": round(float(prediction), 2)
    }