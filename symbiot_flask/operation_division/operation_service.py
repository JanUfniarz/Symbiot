from injector import inject

from client_division.gpt.gpt_client import GPTClient
from symbiot_service import SymbiotService
from .operation_builder import OperationBuilder
from .operation_entity import Operation
from .operation_repository import OperationRepository
from .record.script_record import ScriptRecord
from .record.step_record import StepRecord


class OperationService(SymbiotService):
    @inject
    def __init__(
            self,
            operation_repository: OperationRepository,
            operation_builder: OperationBuilder):
        super().__init__()
        self.repository = operation_repository
        self.builder = operation_builder

    def create(self, wish):
        # command = self.ps_command_generator.save_to_file(
        #     self.gpt_connector.respond(nord_star)
        # )

        print("service, create: " + wish)

        operation = Operation(wish)
        operation.status = "CALIBRATION"
        step_1 = StepRecord([])

        operation.add_record(step_1)
        self.repository.save(operation)

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

    def operations_data(self):
        return self.repository.get_all()
