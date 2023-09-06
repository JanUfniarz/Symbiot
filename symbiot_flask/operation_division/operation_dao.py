from flask_sqlalchemy import SQLAlchemy
from injector import inject

from .record.record_entity import RecordEntity
from .operation_entity import Operation


class OperationDAO:
    @inject
    def __init__(self, db: SQLAlchemy):
        self._db = db

    def add_operation(self, operation):
        if self._db is None:
            raise Exception('db not provided to add')
        print("dao, add: " + operation.name)
        self._db.session.add(operation)
        self._db.session.commit()

    def get_container_by_id(self, id_):
        return self._db.session.query(RecordEntity).get(id_)

    def get_all_operations(self):
        return self._db.session.query(Operation).all()
