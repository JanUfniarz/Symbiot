from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from injector import singleton, Module

from .operation_controller import OperationController
from .operation_dao import OperationDAO
from .operation_service import OperationService


class OperationDivision(Module):
    def __init__(self, app, db):
        self.app = app
        self.db = db

    def configure(self, binder):
        binder.bind(OperationController, scope=singleton)
        binder.bind(Flask, to=self.app)
        binder.bind(OperationService, scope=singleton)
        binder.bind(OperationDAO, scope=singleton)
        binder.bind(SQLAlchemy, to=self.db)
