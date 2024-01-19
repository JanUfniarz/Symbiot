from flask import Flask
from injector import Module


# noinspection PyTypeChecker
class SymbiotDivision(Module):
    def __init__(self):
        self.app: Flask = None
        self.db = None
