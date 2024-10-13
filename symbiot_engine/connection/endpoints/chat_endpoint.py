from flask import Flask, jsonify, request
from injector import inject

from symbiot_engine.control.middlewares.handler_provider import HandlerProvider


class ChatEndpoint:
    @inject
    def __init__(self, app: Flask,
                 handler_provider: HandlerProvider):
        self.app: Flask = app
        self.provider = handler_provider

    def listen(self, path):
        @self.app.route(path + "/prompt", methods=["PUT"])
        def new_message():
            body, must_reload = self.provider.continue_chat(
                request.get_json()["prompt"])
            return jsonify({
                "step_body": body,
                "must_reload": must_reload})

        @self.app.route(path + "/body", methods=["PUT"])
        def set_body():
            self.provider.set_body(request.get_json().get("new_body"))
            return jsonify(dict(message="body updated"))

        @self.app.route(path + "/", methods=["POST"])
        def manage_chat():
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
