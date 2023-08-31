from .operation_entity import Operation
from .container.container_entity import ContainerEntity


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

        self.dao.add_operation(
            Operation("operacja dupa",
                      "chcę sprawdzić czy dodawanie działa",
                      [ContainerEntity("step",
                                       ["0<@bridge>int<@bridge>1",
                                        "1<@bridge>str<@bridge>dupa"],
                                       body="treść rozmowy z gpt")],
                      "nie wiem co w sumie"))

        # operation = Operation(0, "", "", "", "", "", "")

        # kalibracja kompasu

        # zapisanie ścieżki

        # return command, True

    def operations_data(self):
        return self.dao.get_all_operations()
