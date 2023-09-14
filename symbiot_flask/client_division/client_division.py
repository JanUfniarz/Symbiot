from flask import Flask
from injector import singleton, Module

from .client_builder import ClientBuilder
from .client_service import ClientService
from .keys_controller import KeysController


class ClientDivision(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        binder.bind(ClientService, scope=singleton)
        binder.bind(ClientBuilder, scope=singleton)
        binder.bind(KeysController, scope=singleton)
        binder.bind(Flask, to=self.app)
