from injector import inject

from objects.operation import Operation
from operation_division.operation_entity import OperationEntity
from operation_division.record.record_converter import RecordConverter


class OperationConverter:
    @inject
    def __init__(self, record_converter: RecordConverter):
        self.record_converter = record_converter

    def to_entity(self, operation: Operation) -> OperationEntity:
        args = operation.__dict__.copy()
        args["records"] = list(map(lambda record: self.record_converter.to_entity(record),
                                   args["records"]))
        if "_sa_instance_state" in args:
            args.pop("_sa_instance_state")
        return OperationEntity(args.pop("wish", **args))

    def from_entity(self, entity: OperationEntity) -> Operation:
        args = entity.__dict__.copy()
        args["records"] = Operation.join_records(
            list(map(lambda record: self.record_converter.from_entity(record),
                     args["records"])))
        return Operation(**args)
