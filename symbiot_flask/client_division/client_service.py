from injector import inject

from symbiot_service import SymbiotService
from client_division.client_builder import ClientBuilder
from .gpt.gpt_client import GPTClient
from .gpt.gpt_client_repository import GPTClientRepository
from .test_tk import TestTK


class ClientService(SymbiotService):
    @inject
    def __init__(self,
                 client_builder: ClientBuilder,
                 client_repository: GPTClientRepository):
        super().__init__()
        self.builder = client_builder
        self.repository = client_repository

    @staticmethod
    def distribute_keys(open_ai=None):
        def check_clear(key):
            if key == "clear":
                key = None
            return key

        if open_ai is not None:
            GPTClient.set_api_key(check_clear(open_ai))

    def generate_client(self, step):
        return self.builder.add_step(step)

    def calling_test(self):
        print("client")
        tk = TestTK()
        tk.forced = "method"
        client = self.builder.new("gpt").add_access(tk).build()
        # client = GPTClient()
        response = client.chat("write anything and print it using method")
        print(f"response: {response}")


