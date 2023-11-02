from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from injector import singleton

# noinspection PyPackages
from symbiot_lib.components.symbiot_division import SymbiotDivision
from symbiot_server.control.client_builder import ClientBuilder
from symbiot_server.control.client_factory import ClientFactory
from symbiot_server.control.services.client_service import ClientService
from symbiot_server.endpoints.client_endpoint import ClientEndpoint
from symbiot_server.endpoints.keys_endpoint import KeysEndpoint


class ClientDivision(SymbiotDivision):

    def configure(self, binder):
        binder.bind(ClientService, scope=singleton)
        binder.bind(ClientBuilder, scope=singleton)
        binder.bind(KeysEndpoint, scope=singleton)
        binder.bind(ClientFactory, scope=singleton)
        binder.bind(ClientEndpoint, scope=singleton)
        binder.bind(SQLAlchemy, to=self.db)
        binder.bind(Flask, to=self.app)
