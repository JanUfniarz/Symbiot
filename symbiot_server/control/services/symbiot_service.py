from abc import abstractmethod, ABC

from symbiot_server.control.mediator import Mediator


# noinspection PyTypeChecker
class SymbiotService(ABC):
    @abstractmethod
    @property
    def division_name(self):
        pass

    def __init__(self):
        self.mediator: Mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator
