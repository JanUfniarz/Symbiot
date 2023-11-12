from flask import Flask, jsonify, request
from injector import inject

from symbiot_core.handlers.calibration_handler import CalibrationHandler
from symbiot_core.handlers.chat_handler import ChatHandler


class ChatEndpoint:
    @inject
    def __init__(self, app: Flask,
                 calibration_handler: CalibrationHandler):
        self.app: Flask = app
        self._handlers: dict[str, ChatHandler] = dict(
            calibration=calibration_handler
        )
        # noinspection PyTypeChecker
        self._active_handler: ChatHandler = None

    def handler(self, status: str = None) -> ChatHandler:
        def set_handler(status_):
            for el in status_.split("/"):
                if el in self._handlers:
                    self._active_handler = self._handlers[el]

        if status is not None:
            set_handler(status)
        if self._active_handler is None:
            raise ValueError("No active handler, provide proper status")
        return self._active_handler

    def listen(self, path):
        @self.app.route(path + "/prompt", methods=["PUT"])
        def new_message():
            return jsonify({
                "step_body": self.handler().continue_chat(
                    request.get_json()["prompt"])})

        @self.app.route(path + "/body", methods=["PUT"])
        def set_body():
            self.handler().set_body(request.get_json().get("new_body"))
            return jsonify(dict(message="body updated"))

        @self.app.route(path + "/", methods=["POST"])
        def manage_chat():
            data: dict = request.get_json()
            match data.get("command"):
                case "open":
                    self.handler(status=data.get("status")).open_chat(data.get("id"))
                case "close":
                    self.handler().close_chat()
                    self._active_handler = None
                case _:
                    raise ValueError("Invalid command")
            return jsonify({"message": "chat opened"})
