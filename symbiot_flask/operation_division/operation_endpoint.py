from flask import jsonify, Flask, request
from injector import inject

from .operation_service import OperationService


class OperationEndpoint:

    @inject
    def __init__(self, app: Flask,
                 service: OperationService):
        self.app = app
        self.service = service

    def listen(self, path):
        @self.app.route(path + "/", methods=["GET"])
        def get_operations():
            return jsonify(list(map(
                lambda op: op.to_dict(),
                self.service.operations)))

        @self.app.route(path + "/", methods=["PUT"])
        def update_operation():
            # return jsonify({
            #     "message": next(self.service.mediator("creative").gpt.respond(arg))
            # })
            pass

        @self.app.route(path + '/', methods=["POST"])
        def add_operation():
            wish = request.get_json()["wish"]
            self.service.create(wish)
            return jsonify({"message": "added operation"})

        @self.app.route(path + "/", methods=["DELETE"])
        def delete_operation():
            print("start")
            self.service.mediator("client").calling_test()
            print("end")
            return jsonify({"message": "git"})
