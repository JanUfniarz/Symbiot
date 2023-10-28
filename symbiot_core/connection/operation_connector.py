import pickle

import requests

from symbiot_core.connection.pickle_connector import PickleConnector
from symbiot_lib.objects.operation import Operation
from symbiot_lib.objects.step_record import StepRecord


class OperationConnector(PickleConnector):

    def __init__(self):
        super().__init__("operation")

    def get_by_step(self, step: StepRecord) -> Operation:
        response = requests.get(self.url, headers=self.headers, params=dict(
            step=step.to_dict))

        self.check_status(response)

        return pickle.loads(response.json()["pickle"])
