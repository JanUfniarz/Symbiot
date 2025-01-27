from abc import abstractmethod, ABC

from flask import Flask


class SymbiotEndpoint(ABC):
    def __init__(self, app: Flask):
        self.app: Flask = app

    @abstractmethod
    def listen(self, path: str) -> None:
        pass
