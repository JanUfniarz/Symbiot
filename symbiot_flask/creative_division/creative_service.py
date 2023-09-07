from injector import inject

from symbiot_service import SymbiotService
from .gpt.gpt_connector import GPTConnector


class CreativeService(SymbiotService):
    @inject
    def __init__(self, gtp_connector: GPTConnector):
        super().__init__()
        self.gpt = gtp_connector

    def distribute_keys(self, open_ai=None):
        if open_ai is not None:
            self.gpt.set_api_key(open_ai)
