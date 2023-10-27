from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from injector import singleton

# noinspection PyPackages
from .symbiot_division import SymbiotDivision
from symbiot_server.endpoints.chat_endpoint import ChatEndpoint
from symbiot_server.control.client_builder import ClientBuilder
from symbiot_server.database.converters.client_converter import ClientConverter
from symbiot_server.control.client_factory import ClientFactory
from symbiot_server.control.services.client_service import ClientService
from symbiot_server.database.repositories.gpt_client_repository import GPTClientRepository
from symbiot_server.endpoints.keys_endpoint import KeysEndpoint


class ClientDivision(SymbiotDivision):

    def configure(self, binder):
        binder.bind(ClientService, scope=singleton)
        binder.bind(ClientBuilder, scope=singleton)
        binder.bind(KeysEndpoint, scope=singleton)
        binder.bind(ChatEndpoint, scope=singleton)
        binder.bind(ClientFactory, scope=singleton)
        binder.bind(GPTClientRepository, scope=singleton)
        binder.bind(ClientConverter, scope=singleton)
        binder.bind(SQLAlchemy, to=super().db)
        binder.bind(Flask, to=super().app)
