from model_registry import registry

def run(data):

    prediction = registry.get("spam").predict(
        [data["message"]]
    )[0]

    return {
        "tool": "spam",
        "status": "success",
        "prediction": prediction,
    }