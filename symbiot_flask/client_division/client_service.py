from injector import inject

from operation_division.record.step_record import StepRecord
from symbiot_service import SymbiotService
from client_division.client_builder import ClientBuilder
from .gpt.gpt_client import GPTClient
from .gpt.gpt_client_repository import GPTClientRepository
from .test_tk import TestTK


class ClientService(SymbiotService):

    # noinspection PyTypeChecker
    @inject
    def __init__(self,
                 client_builder: ClientBuilder,
                 client_repository: GPTClientRepository):
        super().__init__()
        self.builder: ClientBuilder = client_builder
        self.repository: GPTClientRepository = client_repository
        self.active_step: StepRecord = None

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

    def calibrate(self, step: StepRecord, wish: str):
        client: GPTClient = self.builder.new("gpt", "calibrator").build()
        step.client = client
        self.active_step = step
        self.continue_chat(wish)

    def continue_chat(self, prompt: str):
        step = self.active_step
        response = self.active_step.client.chat()
        step.add_entry(prompt, response)
        return step.body
