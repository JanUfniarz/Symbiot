from flask_sqlalchemy import SQLAlchemy
from injector import inject

from symbiot_lib.objects.record import Record
# noinspection PyPackages
from .symbiot_repository import SymbiotRepository
from symbiot_server.database.converters.operation_converter import OperationConverter
from symbiot_server.database.converters.record_converter import RecordConverter
from symbiot_server.database.entities.record_entity import RecordEntity
from symbiot_server.database.entities.operation_entity import OperationEntity


class OperationRepository(SymbiotRepository):
    @inject
    def __init__(self, db: SQLAlchemy, record_converter: RecordConverter,
                 operation_converter: OperationConverter):
        super().__init__(db, OperationEntity, operation_converter)
        self.record_converter = record_converter

    def get_record_by_id(self, id_) -> Record:
        return self.record_converter.from_entity(
            self.db.session.query(RecordEntity).get(id_))

    def update_record(self, record: Record):
        self.db.session.merge(self.record_converter.to_entity(record))
        self.db.session.commit()
