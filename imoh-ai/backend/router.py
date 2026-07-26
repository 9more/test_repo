from llm import stream_llm
from routes import Route


class GeminiRoute(Route):

    def can_handle(self, message: str) -> bool:
        return True

    def handle(self, message: str):
        yield from stream_llm(message)


ROUTES = [
    GeminiRoute(),
]


def route_request(message: str):

    for route in ROUTES:

        if route.can_handle(message):
            yield from route.handle(message)
            return