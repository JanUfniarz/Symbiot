from injector import inject

from client_division.client_builder import ClientBuilder
from tool_kits.nord_star_extractor import NordStarExtractor
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
        self._builder: ClientBuilder = client_builder
        self._repository: GPTClientRepository = client_repository
        self._active_step: StepRecord = None

    @staticmethod
    def distribute_keys(open_ai=None):
        def check_clear(key):
            if key == "clear":
                key = None
            return key

        if open_ai is not None:
            GPTClient.set_api_key(check_clear(open_ai))

    def open_chat(self, step_id):
        self._active_step = self.mediator("operation")\
            .get_step(step_id)

    def close_chat(self):
        self.mediator("operation").save_step(self._active_step)
        self._active_step = None

    # TAG: calibration
    def calibrate(self, step: StepRecord, wish: str):
        client: GPTClient = self._builder.new("gpt", "calibrator")\
            .add_access(NordStarExtractor(self._builder))

        step.client = client
        step.add_to_status("calibration")
        self._active_step = step
        self.continue_chat(wish)

    def continue_chat(self, prompt: str):
        if not self._active_step:
            # TODO: implement
            raise NotImplementedError("no active step")
        step = self._active_step
        response = self._active_step.client.chat()
        step.add_entry(prompt, response)
        return step.body

    # TAG: calibration
    def calibration_ended(self, nord_star: str, name: str):
        self._active_step.inputs.append(name)
        self._active_step.outputs.append(nord_star)
        self._active_step.add_to_status("done")
        self.mediator("operation").calibration_ended(self._active_step)
