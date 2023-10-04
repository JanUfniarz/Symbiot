from injector import inject

from client_division.client_builder import ClientBuilder
from operation_division.record.step_record import StepRecord
from symbiot_service import SymbiotService
from .gpt.gpt_client import GPTClient
from .gpt.gpt_client_repository import GPTClientRepository


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

    def open_chat(self, step_id):
        self.active_step = self.mediator("operation")\
            .repository.get_record_by_id(step_id)

    def close_chat(self, step_id):
        pass

    def calibrate(self, step: StepRecord, wish: str):
        client: GPTClient = self.builder.new("gpt", "calibrator").build()
        step.client = client
        self.active_step = step
        self.continue_chat(wish)

    def continue_chat(self, prompt: str):
        if not self.active_step:
            # TODO: implement
            raise NotImplementedError("no active step")
        step = self.active_step
        response = self.active_step.client.chat()
        step.add_entry(prompt, response)
        return step.body
