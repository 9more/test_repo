from llm import stream_llm
from routes import Route
from tools.spam import run as spam_run
from tools.sentiment import run as sentiment_run

class GeminiRoute(Route):

    def can_handle(self, message: str, tool: str) -> bool:
        return tool == "gemini"

    def handle(self, message: str):
        yield from stream_llm(message)


class SpamRoute(Route):

    def can_handle(self, message: str, tool: str) -> bool:
        return tool == "spam"

    def handle(self, message: str):
        print("SpamRoute reached")

        result = spam_run({"message": message})

        print(result)

        yield f"Prediction: {result['prediction']}"
       
class SentimentRoute(Route):

    def can_handle(self, message: str, tool: str) -> bool:
        return tool == "sentiment"

    def handle(self, message: str):
        print("SentimentRoute reached")

        result = sentiment_run({"message": message})

        print(result)

        yield f"Prediction: {result['prediction']}"

ROUTES = [
    SpamRoute(),
    SentimentRoute(),
    GeminiRoute(),
]


def route_request(message: str, tool: str):

    print(f"Routing request for tool: {tool}")

    for route in ROUTES:

        print(
            f"Checking {route.__class__.__name__} -> "
            f"{route.can_handle(message, tool)}"
        )

        if route.can_handle(message, tool):
            print(f"Matched {route.__class__.__name__}")
            yield from route.handle(message)
            return

    print("No matching route found")