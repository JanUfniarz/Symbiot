import base64
import pickle
import sys

import requests
from requests import Response


class PickleConnector:
    headers: dict = {'Content-Type': "application/json; charset=UTF-8"}

    def __init__(self, path: str = None):
        self.path = path
        self._docker_mode: bool = '--docker' in sys.argv

    @property
    def url(self) -> str:
        server_host: str = "symbiot-server-1" \
            if self._docker_mode else "127.0.0.1"
        return f"http://{server_host}:5000/"

    @staticmethod
    def check_status(response: Response) -> Response:
        if response.status_code != 200:
            raise Exception(f"Server error: {response.status_code}")
        return response

    def get_pickle(self, params: dict):
        params["expected_format"] = "pickle"
        return pickle.loads(base64.b64decode(self.check_status(
            requests.get(
                self.url + self.path + "/",
                headers=self.headers,
                params=params)).json()["pickle"]))

    def post_pickle(self, object_, path=None):
        return self.check_status(requests.post(
            self.url + (self.path if path is None else path) + "/",
            headers=self.headers,
            json=dict(
                pickle=(base64.b64encode(pickle.dumps(object_)).decode("utf-8")))))


def endpoint(path: str):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            self.path = path
            return func(self, *args, **kwargs)

        return wrapper

    return decorator
