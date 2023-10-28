import pickle

from flask import jsonify, Flask, request
from injector import inject

from symbiot_server.control.services.operation_service import OperationService


class OperationEndpoint:

    @inject
    def __init__(self, app: Flask,
                 service: OperationService):
        self.app = app
        self.service = service

    @staticmethod
    def _format(object_, format_: str = "json"):
        match format_:
            case "json": return jsonify(object_.to_dict())
            case "pickle": return pickle.dumps(object_)

    def listen(self, path):
        @self.app.route(path + "/", methods=["GET"])
        def get_operations():
            args = request.args

            if args is not None and "by" in args:
                return self._format(
                    self.service.operation(args["by"], args["content"]),
                    format_=args.get("format"))
            else:
                return jsonify(list(map(
                    lambda op: self._format(op, args["format"]),
                    self.service.operations)))

        @self.app.route(path + '/', methods=["POST"])
        def add_operation():
            wish = request.get_json()["wish"]
            self.service.create(wish)
            return jsonify({"message": "added operation"})

        # @self.app.route(path +
