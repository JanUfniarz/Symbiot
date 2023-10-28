import pickle

import requests

from symbiot_core.connection.pickle_connector import PickleConnector
from symbiot_lib.objects.gpt_client import GPTClient


class ClientConnector(PickleConnector):

    def __init__(self):
        super().__init__("client")

    def calibrator(self) -> GPTClient:
        response = requests.get(self.url, headers=self.headers, params=dict(
            by="name",
            name="calibrator"))

        self.check_status(response)

        return pickle.loads(response.json()["pickle"])
