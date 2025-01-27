import base64
import pickle

from flask import Flask, request, jsonify, Response
from injector import inject

from symbiot_lib.components.symbiot_endpoint import SymbiotEndpoint
from symbiot_server.control.services.agent_service import AgentService


class AgentEndpoint(SymbiotEndpoint):

    @inject
    def __init__(self, app: Flask,
                 service: AgentService):
        super().__init__(app)
        self.service = service

    def listen(self, path: str) -> None:
        @self.app.route(path + "/", methods=["GET"])
        def get_agent() -> Response:
            params = request.args

            return jsonify(dict(
                pickle=base64.b64encode(pickle.dumps(
                    self.service.new_agent(
                        params["by"],
                        params["content"]))).decode("utf-8")))
