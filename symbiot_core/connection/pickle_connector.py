import pickle

import requests
from requests import Response


class PickleConnector:
    headers: dict = {'Content-Type': "application/json; charset=UTF-8"}
    url = "http://127.0.0.1:5000/"

    def __init__(self, path: str = None):
        self.path = path

    @staticmethod
    def check_status(response: Response) -> Response:
        if response.status_code != 200:
            raise Exception(f"Server error: {response.status_code}")
        return response

    def get_pickle(self, params: dict):
        params["format"] = "pickle"
        return pickle.loads(self.check_status(
            requests.get(
                self.url + self.path,
                headers=self.headers,
                params=params)).json()["pickle"])

    def put_pickle(self, object_, path=None):
        return self.check_status(requests.put(
            self.url + self.path if path is None else path,
            headers=self.headers,
            json=dict(
                pickle=pickle.dumps(object_))))


def endpoint(path):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            self.path = path
            return func(*args, **kwargs)

        return wrapper

    return decorator
