import requests

from symbiot_core.connection.symbiot_connector import SymbiotConnector
from symbiot_lib.objects.step_record import StepRecord


class OperationConnector(SymbiotConnector):

    def __init__(self):
        super().__init__("operation")

    def get_by_step(self, step: StepRecord):
        response = requests.get()
