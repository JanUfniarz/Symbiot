from injector import inject

from symbiot_service import SymbiotService
from .operation_entity import Operation
from .operation_repository import OperationRepository
from .record.step_record import StepRecord


class OperationService(SymbiotService):
    @inject
    def __init__(
            self,
            operation_repository: OperationRepository):
        super().__init__()
        self._repository = operation_repository

    @property
    def operations(self):
        return self._repository.get_all()

    # Endpoint access
    def create(self, wish):
        # command = self.ps_command_generator.save_to_file(
        #     self.gpt_connector.respond(nord_star)
        # )

        print("service, create: " + wish)

        operation = Operation(wish)
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

    def save_step(self, step: StepRecord):
        self._repository.update_record(step)

    def get_step(self, id_: int):
        return self._repository.get_record_by_id(id_)


def calibration_ended(self, step: StepRecord):
    for operation in self.operations:
        if step in operation.records:
            operation.nord_star = step.outputs[0]
            self._repository.save(operation)
    # TODO: go on


"""
        -> client oceniający liczbę potrzebnych kroków
        if (potrzebne więcej scenariuszy): 
            -> inny client układający alternatywne scenariusze
            -> ocena scenariuszy
        -> utworzenie skryptu
        -> walidacja skryptu
        -> zapisanie skryptu u użytkownika
"""
