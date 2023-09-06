from injector import singleton, Module

from .gpt.gpt_connector import GPTConnector
from .creative_service import CreativeService


class CreativeDivision(Module):
    def configure(self, binder):
        binder.bind(CreativeService, scope=singleton)
        binder.bind(GPTConnector)
