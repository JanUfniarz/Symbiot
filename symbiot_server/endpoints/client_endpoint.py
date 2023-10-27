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
            params = request.get_json()

            return jsonify(dict(pickle=pickle.dumps(
                self.service.new_by_name(
                    params["by"],
                    params["content"]))))
