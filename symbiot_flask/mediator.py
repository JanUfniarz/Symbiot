from client_division.client_service import ClientService
from operation_division.operation_service import OperationService


class Mediator:
    def __init__(self, symbiot):
        self._services = dict(
            operation=symbiot.get(OperationService),
            client=symbiot.get(ClientService))
        for service in self._services.values():
            service.set_mediator(self)

    def __call__(self, name):
        return self._services[name]
