from injector import inject

from symbiot_service import SymbiotService
from .operation_builder import OperationBuilder
from .operation_repository import OperationRepository
from .record.record import Record
from .record.record_converter import RecordConverter
from .record.script_record import ScriptRecord
from .record.step_record import StepRecord
from .operation_entity import Operation


class OperationService(SymbiotService):
    @inject
    def __init__(
            self,
            operation_dao: OperationRepository,
            operation_builder: OperationBuilder):
        super().__init__()
        self.dao = operation_dao
        self.builder = operation_builder

    def create(self, nord_star):
        # command = self.ps_command_generator.save_to_file(
        #     self.gpt_connector.respond(nord_star)
        # )

        print("service, create: " + nord_star)

        operation_test = Operation(
            "operacja dupa",
            "chcę sprawdzić czy dodawanie działa",
            "nie wiem co w sumie")

        operation_test.add_record(
            StepRecord(
                [1, "dupa"],
                body="treść rozmowy z gpt"))

        operation_test.add_record(
            ScriptRecord(
                [["dupa", 1], [5.6, True]],
                path="sciezka/do/skryptu",
                previous=1))

        self.dao.save(operation_test)

        # kalibracja kompasu

        # zapisanie ścieżki

        # return command, True

    def operations_data(self):
        return self.dao.get_all()
