import json

from flask import jsonify, Flask
from injector import inject

from .operation_service import OperationService


class OperationController:

    @inject
    def __init__(self, app: Flask, service: OperationService):
        self.app = app
        self.service = service

    def listen(self, path):
        @self.app.route(path + "/", methods=["GET"])
        def get_operation():
            return jsonify(list(map(
                lambda op: op.to_dict(),
                self.service.operations_data())))

        @self.app.route(path + "/", methods=["PUT"])
        def update_operation():
            pass

        @self.app.route(path + '/<string:arg>', methods=["POST"])
        def add_operation(arg):

            # self.service.create(arg)
            # command, execute = service.create(arg)
            #
            # return jsonify(
            #     {"command": command,
            #      "execute": execute})
            # return jsonify({"arg": arg})
            return jsonify({
                "message": self.service.mediator("creative").gpt.respond(arg)
            })

        @self.app.route(path + "/", methods=["DELETE"])
        def guide_delete():
            pass
