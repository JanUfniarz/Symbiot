from flask import Flask
from injector import Injector

from symbiot_lib.components.symbiot_division import SymbiotDivision


# noinspection PyTypeChecker
class SymbiotStarter:
    def __init__(self, endpoints: dict):
        self.endpoints = endpoints
        self._app = None
        self._injector: Injector = None

    def __call__(self, cls):
        return self._injector.get(cls)

    def divisions(self, divisions: list[SymbiotDivision]):
        if self._app is None:
            raise ValueError("provide flask app first")
        for div in divisions:
            div.app = self._app
        self._injector = Injector(divisions)
        return self

    def flask(self, app: Flask):
        self._app = app
        return self

    def listen_all(self, excluded: list = None):
        if not excluded:
            excluded = []
        for key, value in {
            k: v for k, v in self.endpoints.items()
                if k not in excluded}.items():
            self(value).listen(f"/{key}")
        return self

    def run(self, **kwargs):
        self._app.run(**kwargs)
        return self
