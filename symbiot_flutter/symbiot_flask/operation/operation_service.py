# from .operation_entity import Operation


def dir_database():
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '..', 'database')))


class OperationService:
    def __init__(self, gpt_connector, ps_command_generator, dao):
        self.gpt_connector = gpt_connector
        self.ps_command_generator = ps_command_generator
        self.dao = dao

    def create(self, nord_star):

        # command = self.ps_command_generator.save_to_file(
        #     self.gpt_connector.respond(nord_star)
        # )
        dir_database()
        from e import E

        self.dao.add(E("dupa"))

        # operation = Operation(0, "", "", "", "", "", "")


        # kalibracja kompasu




        # zapisanie ścieżki

        # return command, True
