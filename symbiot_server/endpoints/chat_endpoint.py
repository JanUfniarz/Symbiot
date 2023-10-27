from flask import Flask, jsonify, request
from injector import inject

from client_division.client_service import ClientService


class ChatEndpoint:
    @inject
    def __init__(self, app: Flask,
                 client_service: ClientService):
        self.app = app
        self.service = client_service

    def listen(self, path):
        @self.app.route(path + "/", methods=["PUT"])
        def new_message():
            return jsonify({
                "step_body": self.service.continue_chat(
                    request.get_json()["prompt"])})

        @self.app.route(path + "/", methods=["POST"])
        def manage_chat():
            command = request.get_json()["command"]
            step_id = request.get_json()["id"]
            match command:
                case "open":
                    self.service.open_chat(step_id)
                case "close":
                    self.service.close_chat()
                case _:
                    raise ValueError("Invalid command")
            return jsonify(
                {"message": f"chat of step {step_id} {command}"})
