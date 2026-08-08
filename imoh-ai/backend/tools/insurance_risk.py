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
        "insurance_risk"
    ).predict(df)[0]

    return {
        "tool": "insurance_risk",
        "status": "success",
        "prediction": prediction,
    }