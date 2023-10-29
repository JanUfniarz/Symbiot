import pickle
from itertools import chain

from flask import jsonify, Flask, request
from injector import inject

from symbiot_lib.objects.record import Record
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
            return list(map(
                lambda op: self._format(op, self._data().get("expected_format")),
                self.service.operations))

        @self.app.route(path + '/', methods=["POST"])
        def add_operation():
            wish = request.get_json()["wish"]
            self.service.create(wish)
            return jsonify({"message": "added operation"})

        @self.app.route(path + "/records", methods=["GET"])
        def get_records():
            if "by" in self._data():
                return self._format(
                    self.service.record(self._data()["by"], self._data()["content"]),
                    format_=self._data().get("expected_format"))
            return list(map(
                lambda record: self._format(
                    record, self._data().get("expected_format")),
                list(chain.from_iterable(map(
                    lambda operation: operation.records,
                    self.service.operations)))))

        @self.app.route(path + "/record", methods=["POST"])
        def add_record():
            if "pickle" in self._data(json=True):
                self.service.save_record(
                    pickle.loads(self._data(json=True).get("pickle")))
            return jsonify({"message": "added record"})
