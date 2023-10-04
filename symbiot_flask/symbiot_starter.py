from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from injector import Injector

from client_division.chat_endpoint import ChatEndpoint
from client_division.keys_endpoint import KeysEndpoint
from mediator import Mediator
from operation_division.operation_endpoint import OperationEndpoint
from operation_division.operation_entity import Operation
from operation_division.record.record import Record
from operation_division.record.record_converter import RecordConverter
from symbiot_division import SymbiotDivision


# noinspection PyTypeChecker
class SymbiotStarter:
    _endpoints: dict = dict(
        operation=OperationEndpoint,
        key=KeysEndpoint,
        chat=ChatEndpoint)

    def __init__(self):
        self._injector: Injector = None
        self._mediator: Mediator = None
        self._record_converter: RecordConverter = None

    def __call__(self, cls):
        if cls is Mediator:
            return self._mediator
        if cls is RecordConverter:
            return self._record_converter
        return self._injector.get(cls)

    @property
    def _app(self):
        if not SymbiotDivision.app:
            raise Exception("provide flask app first")
        return SymbiotDivision.app

    @_app.setter
    def _app(self, value):
        SymbiotDivision.app = value

    @property
    def _db(self):
        if not SymbiotDivision.db:
            raise Exception("provide sqlAlchemy db first")
        return SymbiotDivision.db

    @_db.setter
    def _db(self, value):
        SymbiotDivision.db = value

    def divisions(self, divisions: list):
        self._injector = Injector(divisions)
        self._mediator = Mediator(self._injector)
        return self

    def flask(self, app: Flask):
        self._app = app
        return self

    def sql_alchemy(self, db: SQLAlchemy, path: str):
        self._app.config['SQLALCHEMY_DATABASE_URI'] = path
        db.init_app(self._app)
        self._db = db
        return self

    def converters(self, record_converter: RecordConverter):
        self._record_converter = record_converter
        for cls in [Operation, Record]:
            cls.set_converter(record_converter)
        return self

    def rebuild_database(self):
        with self._app.app_context():
            self._db.drop_all()
            self._db.create_all()
        return self

    def listen_all(self, excluded: list = None):
        if not excluded:
            excluded = []
        for key, value in {
            k: v for k, v in self._endpoints.items()
                if k not in excluded}.items():
            self(value).listen(f"/{key}")
        return self

    def run(self):
        self._app.run(debug=True)
        return self
