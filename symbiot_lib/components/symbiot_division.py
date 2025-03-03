from abc import abstractmethod

from flask import Flask
from injector import Module, Binder


class SymbiotDivision(Module):
    def __init__(self):
        self.app: Flask | None = None
        self.db = None

    @abstractmethod
    def configure(self, binder: Binder) -> None:
        pass
