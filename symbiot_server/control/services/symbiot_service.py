from abc import abstractmethod, ABC

from symbiot_server.control.mediator import Mediator


class SymbiotService(ABC):
    @abstractmethod
    def division_name(self) -> str:
        pass

    def __init__(self):
        self.mediator: Mediator | None = None

    def set_mediator(self, mediator: Mediator) -> None:
        self.mediator = mediator
