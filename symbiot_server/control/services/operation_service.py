from injector import inject

from symbiot_lib.objects.operation import Operation
from symbiot_lib.objects.record import Record
from symbiot_lib.objects.step_record import StepRecord
from symbiot_server.database.entities.operation_entity import OperationEntity
from symbiot_server.database.repositories.operation_repository import OperationRepository
# noinspection PyPackages
from .symbiot_service import SymbiotService


class OperationService(SymbiotService):
    division_name = "operation"

    @inject
    def __init__(
            self,
            operation_repository: OperationRepository):
        super().__init__()
        self._repository = operation_repository

    @property
    def operations(self) -> list[Operation]:
        return self._repository.get_all()

    def create(self, wish):
        # command = self.ps_command_generator.save_to_file(
        #     self.gpt_connector.respond(nord_star)
        # )

        print("service, create: " + wish)

        operation = OperationEntity(wish)
        operation.status = "CALIBRATION"
        step_1 = StepRecord([])

        operation.add_record(step_1)
        self._repository.save(operation)

        self.mediator("client").calibrate(step_1, wish)

        # operation_test = Operation(
        #     "operacja dupa",
        #     "chcę sprawdzić czy dodawanie działa",
        #     "nie wiem co w sumie")
        #
        # operation_test.add_record(
        #     StepRecord(
        #         [1, "dupa"],
        #         body="treść rozmowy z gpt"))
        #
        # operation_test.add_record(
        #     ScriptRecord(
        #         [["dupa", 1], [5.6, True]],
        #         path="sciezka/do/skryptu",
        #         previous=1))

        # self.dao.save(operation_test)

        # kalibracja kompasu

        # zapisanie ścieżki

        # return command, True

    def save_record(self, record: Record):
        self._repository.update_record(record)

    def get_record(self, id_: int):
        return self._repository.get_record_by_id(id_)

    def calibration_ended(self, step: StepRecord):
        for operation in self.operations:
            if step in operation._records:
                operation.name = step.inputs[0]
                operation.nord_star = step.outputs[0]
                # TODO: operation.status = ""
                self._repository.save(operation)
        # TODO: go on

    def operation(self, by: str, content) -> Operation:
        match by:
            case "record_id":
                for operation in self.operations:
                    if content in [record.id for record in operation.records]:
                        return operation
                    raise ValueError(f"no record with id: {content}")
            case _: raise NotImplementedError(f"not implemented operation by {by}")

    def record(self, by: str, content) -> Record:
        match by:
            case "id": return self.get_record(content)
            case _: raise NotImplementedError(f"not implemented operation by {by}")


"""
        -> client oceniający liczbę potrzebnych kroków
        if (potrzebne więcej scenariuszy): 
            -> inny client układający alternatywne scenariusze
            -> ocena scenariuszy
        -> utworzenie skryptu
        -> walidacja skryptu
        -> zapisanie skryptu u użytkownika
"""
