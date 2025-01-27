from flask import Flask
from injector import Binder, singleton

from symbiot_engine.connection.connectors.object_connector import ObjectConnector
from symbiot_engine.connection.endpoints.chat_endpoint import ChatEndpoint
from symbiot_engine.connection.endpoints.keys_endpoint import KeysEndpoint
from symbiot_engine.connection.endpoints.main_endpoint import MainEndpoint
from symbiot_engine.control.handlers.calibration_handler import CalibrationHandler
from symbiot_lib.components.symbiot_division import SymbiotDivision


class EngineDivision(SymbiotDivision):
    def configure(self, binder: Binder) -> None:
        binder.bind(Flask, self.app)
        binder.bind(MainEndpoint, scope=singleton)
        binder.bind(ChatEndpoint, scope=singleton)
        binder.bind(KeysEndpoint, scope=singleton)
        binder.bind(CalibrationHandler, scope=singleton)
        binder.bind(ObjectConnector, scope=singleton)
