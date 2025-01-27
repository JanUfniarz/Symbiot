from flask import Flask, request, jsonify, Response
from injector import inject

from symbiot_lib.components.symbiot_endpoint import SymbiotEndpoint
from symbiot_lib.objects.gpt_agent import GPTAgent


class KeysEndpoint(SymbiotEndpoint):
    @inject
    def __init__(self, app: Flask):
        super().__init__(app)

    @staticmethod
    def distribute_keys(open_ai: str | None = None):
        def check_clear(key: str) -> str | None:
            if key == "clear":
                key = None
            return key

        if open_ai is not None:
            GPTAgent.set_api_key(check_clear(open_ai))

    def listen(self, path: str) -> None:
        @self.app.route(path + "/", methods=['POST'])
        def provide_keys() -> Response:
            keys = request.get_json()
            print("provide")
            self.distribute_keys(
                open_ai=keys["openAI"] if "openAI" in keys else None)
            print(keys["openAI"])
            return jsonify(dict(message="Keys are delivered to server"))

        @self.app.route(path + "/<string:name>", methods=['DELETE'])
        def clear_key(name: str) -> Response:
            self.distribute_keys(
                open_ai="clear" if name == "openAI" else None)
            return jsonify(dict(message=f"{name} key removed"))
