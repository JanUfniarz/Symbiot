from injector import inject

from symbiot_service import SymbiotService
from client_division.client_builder import ClientBuilder
from .gpt.gpt_client import GPTClient


class ClientService(SymbiotService):
    @inject
    def __init__(self, client_builder: ClientBuilder):
        super().__init__()
        self.builder = client_builder

    @staticmethod
    def distribute_keys(open_ai=None):
        def check_clear(key):
            if key == "clear":
                key = None
            return key

        if open_ai is not None:
            GPTClient.set_api_key(check_clear(open_ai))

    def generate_client(self, step):
        return self.builder.add_messages(step)
