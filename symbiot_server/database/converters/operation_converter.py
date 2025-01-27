from injector import inject

from symbiot_lib.objects.operation import Operation
from symbiot_server.database.converters.record_converter import RecordConverter
from symbiot_server.database.entities.operation_entity import OperationEntity


class OperationConverter:
    @inject
    def __init__(self, record_converter: RecordConverter):
        self.record_converter: RecordConverter = record_converter

    def to_entity(self, operation: Operation) -> OperationEntity:
        args = operation.__dict__.copy()
        args["records"] = list(map(lambda record: self.record_converter.to_entity(record),
                                   args.pop("_records")))
        if "_sa_instance_state" in args:
            args.pop("_sa_instance_state")
        args["id_"] = args.pop("id")
        return OperationEntity(args.pop("wish"), **args)

    def from_entity(self, entity: OperationEntity) -> Operation:
        args = entity.__dict__.copy()
        args["records"] = Operation.join_records(
            list(map(lambda record: self.record_converter.from_entity(record),
                     args["records"])))
        if "_sa_instance_state" in args:
            args.pop("_sa_instance_state")
        args["id_"] = args.pop("id")
        return Operation(**args)
