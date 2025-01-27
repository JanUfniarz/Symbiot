from flask import Flask, request, jsonify, Response
from injector import inject

from symbiot_engine.control.handlers.calibration_handler import CalibrationHandler
from symbiot_lib.components.symbiot_endpoint import SymbiotEndpoint


class MainEndpoint(SymbiotEndpoint):

    @inject
    def __init__(self, app: Flask,
                 calibration_handler: CalibrationHandler):
        super().__init__(app)
        self.calibration_handler = calibration_handler

    def listen(self, path: str) -> None:
        @self.app.route(path + "/", methods=["POST"])
        def new_operation() -> Response:
            wish = request.get_json()["wish"]
            self.calibration_handler.create(wish)
            return jsonify({"message": "added operation"})
