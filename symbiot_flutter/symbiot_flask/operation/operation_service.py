from .container.script_container import ScriptContainer
from .container.step_container import StepContainer
from .operation_entity import Operation


class OperationService:
    def __init__(self, gpt_connector, ps_command_generator,
                 dao):
        self.gpt_connector = gpt_connector
        self.ps_command_generator = ps_command_generator
        self.dao = dao

    def create(self, nord_star):
        # command = self.ps_command_generator.save_to_file(
        #     self.gpt_connector.respond(nord_star)
        # )

        print("service, create: " + nord_star)

        operation_test = Operation(
            "operacja dupa",
            "chcę sprawdzić czy dodawanie działa",
            "nie wiem co w sumie")

        operation_test.add_container(
            StepContainer(
                [1, "dupa"],
                body="treść rozmowy z gpt"))

        operation_test.add_container(
            ScriptContainer(
                [["dupa", 1], [5.6, True]],
                path="sciezka/do/skryptu",
                previous=1))

        self.dao.add_operation(operation_test)

        # kalibracja kompasu

        # zapisanie ścieżki

        # return command, True

    def operations_data(self):
        return self.dao.get_all_operations()
