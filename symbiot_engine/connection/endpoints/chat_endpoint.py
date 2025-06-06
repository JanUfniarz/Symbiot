from flask import Flask, jsonify, request, Response
from injector import inject

from symbiot_engine.control.middlewares.handler_provider import HandlerProvider
from symbiot_lib.components.symbiot_endpoint import SymbiotEndpoint


class ChatEndpoint(SymbiotEndpoint):
    @inject
    def __init__(self, app: Flask,
                 handler_provider: HandlerProvider):
        super().__init__(app)
        self.provider = handler_provider

    def listen(self, path: str) -> None:
        @self.app.route(path + "/prompt", methods=["PUT"])
        def new_message() -> Response:
            body, must_reload = self.provider.continue_chat(
                request.get_json()["prompt"])
            return jsonify({
                "step_body": body,
                "must_reload": must_reload})

        @self.app.route(path + "/body", methods=["PUT"])
        def set_body() -> Response:
            self.provider.set_body(request.get_json().get("new_body"))
            return jsonify(dict(message="body updated"))

        @self.app.route(path + "/", methods=["POST"])
        def manage_chat() -> Response:
            data: dict = request.get_json()
            match data.get("command"):
                case "open":
                    self.provider.open_chat(data.get("status"), data.get("id"))
                case "close":
                    self.provider.close_chat()
                    self._active_handler = None
                case _:
                    raise ValueError("Invalid command")
            return jsonify({"message": "chat opened"})
