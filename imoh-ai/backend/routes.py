from abc import ABC, abstractmethod


class Route(ABC):
    """Base class for all routes."""

    @abstractmethod
    def can_handle(self, message: str) -> bool:
        pass

    @abstractmethod
    def handle(self, message: str):
        pass