from flask import Flask
from injector import singleton, Module

from .gpt.gpt_connector import GPTConnector
from .creative_service import CreativeService
from .keys_controller import KeysController


class CreativeDivision(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        binder.bind(CreativeService, scope=singleton)
        binder.bind(GPTConnector)
        binder.bind(KeysController, scope=singleton)
        binder.bind(Flask, to=self.app)
