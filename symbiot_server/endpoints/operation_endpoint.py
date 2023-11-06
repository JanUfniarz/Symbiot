import base64
import pickle
from itertools import chain

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
    def _format(object_, format_: str = "json") -> dict:
        format_ = "json" if format_ is None else format_
        match format_:
            case "json": return object_.serialized
            case "pickle": return dict(
                pickle=base64.b64encode(
                    pickle.dumps(object_)
                ).decode("utf-8"))

    @staticmethod
    def _pickle_decode(encoded):
        return pickle.loads(base64.b64decode(encoded))

    @staticmethod
    def _data(json: bool = False) -> dict:
        args = request.get_json() \
            if json else request.args

        if args is None:
            args = dict()
        return args

    def listen(self, path):
        @self.app.route(path + "/", methods=["GET"])
        def get_operations():
            if "by" in self._data():
                return self._format(
                    self.service.operation(self._data()["by"], self._data()["content"]),
                    format_=self._data().get("expected_format"))
            return jsonify(list(map(
                lambda op: self._format(op, self._data().get("expected_format")),
                self.service.operations)))

        @self.app.route(path + '/', methods=["PUT"])
        def add_operation():
            self.service.save_operation(
                self._pickle_decode(request.get_json()["pickle"]))
            return jsonify(dict(message="added operation"))

        @self.app.route(path + '/', methods=["DELETE"])
        def delete_operation():
            print("del")
            print(self._data(json=True))
            message = self.service.delete_operation(self._data(json=True)["id"])
            print(f"message: {message}")
            return jsonify(dict(
                message=message))

        @self.app.route(path + "/record/", methods=["GET"])
        def get_records():
            if "by" in self._data():
                return self._format(
                    self.service.record(self._data()["by"], self._data()["content"]),
                    format_=self._data().get("expected_format"))
            return list(map(
                lambda record: self._format(
                    record, format_=self._data().get("expected_format")),
                list(chain.from_iterable(map(
                    lambda operation: operation.records,
                    self.service.operations)))))

        @self.app.route(path + "/record/", methods=["PUT"])
        def add_record():
            if "pickle" in self._data(json=True):
                self.service.save_record(
                    self._pickle_decode(self._data(json=True).get("pickle")))
            return jsonify({"message": "added record"})
