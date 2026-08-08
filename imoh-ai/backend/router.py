from llm import stream_llm
from routes import Route
from tools.spam import run as spam_run
from tools.sentiment import run as sentiment_run
from tools.insurance_predictor import run as insurance_predictor_run
from tools.insurance import run as insurance_run


class GeminiRoute(Route):

    def can_handle(self, message: str, tool: str) -> bool:
        return tool == "gemini"

    def handle(self, data):
        yield from stream_llm(data["message"])


class SpamRoute(Route):

    def can_handle(self, data, tool: str) -> bool:
        return tool == "spam"

    def handle(self, data):
        print("SpamRoute reached")

        result = spam_run(data)

        print(result)

        yield f"Prediction: {result['prediction']}"


class SentimentRoute(Route):

    def can_handle(self, data, tool: str) -> bool:
        return tool == "sentiment"

    def handle(self, data):
        print("SentimentRoute reached")

        result = sentiment_run(data)

        print(result)

        yield f"Prediction: {result['prediction']}"


class InsurancePredictorRoute(Route):

    def can_handle(self, data, tool: str):

        return tool == "insurance_predictor"

    def handle(self, data):

        result = insurance_predictor_run(data)

        yield f"Estimated Annual Charge: £{result['prediction']:,.2f}"


class InsuranceRoute(Route):

    def can_handle(self, data, tool):

        return tool == "insurance"

    def handle(self, data):

        result = insurance_run(data)

        yield (
            f"Estimated Annual Charge: "
            f"£{result['charge']:,.2f};\n\n"
            f"Risk Classification: "
            f"{result['risk']}"
        )


ROUTES = [
    SpamRoute(),
    SentimentRoute(),
    InsurancePredictorRoute(),
    GeminiRoute(),
    InsuranceRoute(),
]


def route_request(data, tool: str):

    print(f"Routing request for tool: {tool}")

    for route in ROUTES:

        print(
            f"Checking {route.__class__.__name__} -> " f"{route.can_handle(data, tool)}"
        )

        if route.can_handle(data, tool):
            print(f"Matched {route.__class__.__name__}")
            yield from route.handle(data)
            return

    print("No matching route found")
