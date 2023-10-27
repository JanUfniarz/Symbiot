from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from injector import Injector

from symbiot_server.endpoints.chat_endpoint import ChatEndpoint
from symbiot_server.endpoints.keys_endpoint import KeysEndpoint
from symbiot_server.control.mediator import Mediator
from symbiot_server.endpoints.operation_endpoint import OperationEndpoint
from symbiot_server.database.converters.record_converter import RecordConverter
from symbiot_server.config.divisions.server_division import ServerDivision


# noinspection PyTypeChecker
class SymbiotStarter:
    port: int = 5000
    _endpoints: dict = dict(
        operation=OperationEndpoint,
        key=KeysEndpoint,
        chat=ChatEndpoint)

    def __init__(self):
        self._injector: Injector = None
        self._mediator: Mediator = None

    def __call__(self, cls):
        if cls is Mediator:
            return self._mediator
        return self._injector.get(cls)

    @property
    def _app(self):
        if not ServerDivision.app:
            raise Exception("provide flask app first")
        return ServerDivision.app

    @_app.setter
    def _app(self, value):
        ServerDivision.app = value

    @property
    def _db(self):
        if not ServerDivision.db:
            raise Exception("provide sqlAlchemy db first")
        return ServerDivision.db

    @_db.setter
    def _db(self, value):
        ServerDivision.db = value

    def divisions(self, divisions: list):
        self._injector = Injector(divisions)
        return self

    def mediator(self):
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
        self._app.run(debug=True, port=self.port)
        return self
