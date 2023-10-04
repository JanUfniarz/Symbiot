from flask_sqlalchemy import SQLAlchemy
from injector import inject

from symbiot_repository import SymbiotRepository
from .record.record_entity import RecordEntity
from .operation_entity import Operation


class OperationRepository(SymbiotRepository):
    @inject
    def __init__(self, db: SQLAlchemy):
        super().__init__(db, Operation)

    def get_record_by_id(self, id_):
        return self._db.session.query(RecordEntity).get(id_)
