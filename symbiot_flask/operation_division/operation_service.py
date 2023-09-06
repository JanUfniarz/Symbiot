from injector import inject

from .operation_dao import OperationDAO
from .record.script_record import ScriptRecord
from .record.step_record import StepRecord
from .operation_entity import Operation


class OperationService:
    @inject
    def __init__(self, operation_dao: OperationDAO):
        self.dao = operation_dao

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

        self.dao.add_operation(operation_test)

        # kalibracja kompasu

        # zapisanie ścieżki

        # return command, True

    def operations_data(self):
        return self.dao.get_all_operations()
