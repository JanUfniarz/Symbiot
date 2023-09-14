from creative_division.creative_service import CreativeService
from operation_division.operation_service import OperationService


class Mediator:
    def __init__(self, symbiot):
        self._services = dict(
            operation=symbiot.get(OperationService),
            creative=symbiot.get(CreativeService))
        for service in self._services.values():
            service.set_mediator(self)

    def __call__(self, name):
        return self._services[name]
