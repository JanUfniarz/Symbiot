from flask import Flask, request, jsonify
from injector import inject

from symbiot_core.control.handlers.calibration_handler import CalibrationHandler


class MainEndpoint:

    @inject
    def __init__(self, app: Flask,
                 calibration_handler: CalibrationHandler):
        self.app = app
        self.calibration_handler = calibration_handler

    def listen(self, path):
        @self.app.route(path + "/", methods=["POST"])
        def new_operation():
            wish = request.get_json()["wish"]
            self.calibration_handler.create(wish)
            return jsonify({"message": "added operation"})
