from symbiot_server.control.mediator import Mediator


# noinspection PyTypeChecker
class SymbiotService:
    def __init__(self):
        self.mediator: Mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator
