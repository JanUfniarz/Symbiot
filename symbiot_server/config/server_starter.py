from flask_sqlalchemy import SQLAlchemy

from symbiot_lib.components.symbiot_division import SymbiotDivision
from symbiot_lib.components.symbiot_starter import SymbiotStarter
from symbiot_server.control.mediator import Mediator
from symbiot_server.endpoints.agent_endpoint import AgentEndpoint
from symbiot_server.endpoints.operation_endpoint import OperationEndpoint


# noinspection PyTypeChecker
class ServerStarter(SymbiotStarter):
    def __init__(self):
        super().__init__(dict(
            operation=OperationEndpoint,
            agent=AgentEndpoint))
        self._mediator: Mediator = None
        self._db: SQLAlchemy = None

    def __call__(self, cls):  # * override
        if cls is Mediator:
            return self._mediator
        return self._injector.get(cls)

    def mediator(self):
        self._mediator = Mediator(self._injector)
        return self

    def divisions(
            self,
            divisions: list[SymbiotDivision]):  # * override
        if self._db is None:
            raise ValueError("provide database first")
        for div in divisions:
            div.db = self._db
        super().divisions(divisions)
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
