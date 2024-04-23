from flask import Flask
from injector import Binder, singleton

from symbiot_core.connection.connectors.object_connector import ObjectConnector
from symbiot_core.connection.endpoints.chat_endpoint import ChatEndpoint
from symbiot_core.connection.endpoints.keys_endpoint import KeysEndpoint
from symbiot_core.connection.endpoints.main_endpoint import MainEndpoint
from symbiot_core.control.handlers.calibration_handler import CalibrationHandler
from symbiot_lib.components.symbiot_division import SymbiotDivision


class CoreDivision(SymbiotDivision):
    def configure(self, binder: Binder):
        binder.bind(Flask, self.app)
        binder.bind(MainEndpoint, scope=singleton)
        binder.bind(ChatEndpoint, scope=singleton)
        binder.bind(KeysEndpoint, scope=singleton)
        binder.bind(CalibrationHandler, scope=singleton)
        binder.bind(ObjectConnector, scope=singleton)
