from .record.script_record import ScriptRecord
from .record.step_record import StepRecord
from .operation_entity import Operation


class OperationService:
    def __init__(self, ps_command_generator,
                 operation_dao):
        self._creative = None
        self.ps_command_generator = ps_command_generator
        self.dao = operation_dao

    def wire_creative_division(self, value):
        if self._creative is None:
            self._creative = value
        else:
            print("creative division already wired")

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
