from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from injector import Module


# noinspection PyTypeChecker
class SymbiotDivision(Module):
    def __init__(self):
        self.app: Flask = None
        self.db: SQLAlchemy = None
