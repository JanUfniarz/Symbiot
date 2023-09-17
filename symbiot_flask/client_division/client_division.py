from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from injector import singleton

from symbiot_division import SymbiotDivision
from .client_builder import ClientBuilder
from .client_factory import ClientFactory
from .client_service import ClientService
from .gpt.gpt_client_repository import GPTClientRepository
from .keys_controller import KeysController


class ClientDivision(SymbiotDivision):

    def configure(self, binder):
        binder.bind(ClientService, scope=singleton)
        binder.bind(ClientBuilder, scope=singleton)
        binder.bind(KeysController, scope=singleton)
        binder.bind(ClientFactory, scope=singleton)
        binder.bind(GPTClientRepository, scope=singleton)
        binder.bind(SQLAlchemy, to=super().db)
        binder.bind(Flask, to=super().app)
