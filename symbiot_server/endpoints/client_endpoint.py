import base64
import pickle

from flask import Flask, request, jsonify
from injector import inject

from symbiot_server.control.services.client_service import ClientService


class ClientEndpoint:

    @inject
    def __init__(self, app: Flask,
                 service: ClientService):
        self.app = app
        self.service = service

    def listen(self, path):
        @self.app.route(path + "/", methods=["GET"])
        def get_client():
            params = request.args

            return jsonify(dict(
                pickle=base64.b64encode(pickle.dumps(
                    self.service.new_client(
                        params["by"],
                        params["content"]))).decode("utf-8")))
