from injector import inject

from symbiot_service import SymbiotService
from .gpt.gpt_connector import GPTConnector
import client_division.gpt.client_step_converter as converter


class ClientService(SymbiotService):
    @inject
    def __init__(self, gtp_connector: GPTConnector):
        super().__init__()
        self.gpt = gtp_connector

    def distribute_keys(self, open_ai=None):
        def check_clear(key):
            if key == "clear":
                key = None
            return key

        if open_ai is not None:
            self.gpt.set_api_key(check_clear(open_ai))

    @staticmethod
    def generate_client(step):
        return converter.to_client(step)
    # TODO: add other ways to create

