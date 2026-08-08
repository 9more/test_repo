from model_registry import registry


def run(data):

    prediction = registry.get("sentiment").predict(
        [data["message"]]
    )[0]

    return {
        "tool": "sentiment",
        "status": "success",
        "prediction": prediction,
    }