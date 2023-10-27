from flask import Flask
from injector import Module, Binder, singleton

from symbiot_core.handlers.calibration_handler import CalibrationHandler
from symbiot_core.connection.client_connector import ClientConnector
from symbiot_core.endpoints.main_endpoint import MainEndpoint


class CoreDivision(Module):
    def __init__(self, app: Flask):
        self.app = app

    def configure(self, binder: Binder):
        binder.bind(Flask, self.app)
        binder.bind(MainEndpoint, scope=singleton)
        binder.bind(CalibrationHandler, scope=singleton)
        binder.bind(ClientConnector, scope=singleton)
