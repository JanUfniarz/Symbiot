from requests import Response


class SymbiotConnector:
    headers: dict = {'Content-Type': "application/json; charset=UTF-8"}

    def __init__(self, path: str):
        self.url = "http://127.0.0.1:5000/" + path

    @staticmethod
    def check_status(response: Response):
        if response.status_code != 200:
            raise Exception(f"Server error: {response.status_code}")
