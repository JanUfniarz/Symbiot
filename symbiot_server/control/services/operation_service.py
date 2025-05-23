from injector import inject

from symbiot_lib.objects.operation import Operation
from symbiot_lib.objects.record import Record
from symbiot_server.database.repositories.operation_repository import OperationRepository
# noinspection PyPackages
from .symbiot_service import SymbiotService


def operation_required():
    # * id must be first argument
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            if not self._repository.is_available(args[0]):
                return f"there is no operation with id: {args[0]}"
            return method(self, *args, **kwargs)
        return wrapper
    return decorator


class OperationService(SymbiotService):
    division_name = "operation"

    @inject
    def __init__(
            self,
            operation_repository: OperationRepository):
        super().__init__()
        self._repository: OperationRepository = operation_repository

    @property
    def operations(self) -> list[Operation]:
        return self._repository.get_all()

    def save_record(self, record: Record) -> None:
        if self._repository.is_available(record.id, "records"):
            operation = self.operation("record_id", record.id)
            if record.in_status("TO=calibration", "ns_generated") \
                    and not record.in_status("done"):

                operation.name = record.inputs[0]
                operation.nord_star = record.outputs[0]
                self.save_operation(operation)

                record.add_to_status("done")
            self._repository.update_record(record)
        else:
            operation = self.operation("record_id", record.previous.id)
            operation.add_or_update_record(record)
            self.save_operation(operation)

    def get_record(self, id_: str) -> Record | None:
        return self._repository.get_record_by_id(id_)

    def operation(self, by: str, content) -> Operation | None:
        def condition(operation_: Operation) -> bool:
            match by:
                case "id": return operation_.id == content
                case "record_id": return (
                        content in
                        [record.id for record in operation_.records])
                case _:
                    raise NotImplementedError(f"not implemented operation by {by}")

        try:
            return [operation for operation in self.operations if condition(operation)][0]
        except IndexError:
            return None

    def record(self, by: str, content) -> Record:
        match by:
            case "id":
                return self.get_record(content)
            case _:
                raise NotImplementedError(f"not implemented operation by {by}")

    def save_operation(self, operation):
        self._repository.save(operation)

    @operation_required()
    def delete_operation(self, id_: str) -> str:
        self._repository.delete(id_)
        return "operation deleted"

    @operation_required()
    def update_operation(self, id_: str, to_change: str, value) -> str:
        self._repository.update_value(id_, to_change, value)
        return f"operation {to_change} updated"
