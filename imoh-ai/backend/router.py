from llm import stream_llm
from routes import Route
from tools.spam import run

class GeminiRoute(Route):

    def can_handle(self, message: str, tool: str) -> bool:
        return tool == "gemini"

    def handle(self, message: str):
        yield from stream_llm(message)


class SpamRoute(Route):

    def can_handle(self, message: str, tool: str) -> bool:
        return tool == "spam"

    def handle(self, message: str):
       result = run({"message": message})
       yield f"Prediction: {result['prediction']}"

ROUTES = [
    SpamRoute(),
    GeminiRoute(),
]


def route_request(message: str, tool: str):

    for route in ROUTES:

        if route.can_handle(message, tool):
            yield from route.handle(message)
            return