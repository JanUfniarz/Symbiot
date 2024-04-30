from injector import inject

from symbiot_lib.objects.gpt_client import GPTClient
from symbiot_server.control.client_builder import ClientBuilder
from symbiot_server.control.services.symbiot_service import SymbiotService


class ClientService(SymbiotService):
    division_name = "client"

    # noinspection PyTypeChecker
    @inject
    def __init__(self,
                 client_builder: ClientBuilder):
        super().__init__()
        self._builder: ClientBuilder = client_builder

    def new_client(self, by: str, content) -> GPTClient:
        match by:
            case "name": return self._builder.new("gpt", content).get()
