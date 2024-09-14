from abc import ABC, abstractmethod


class HandlerInterface(ABC):
    @abstractmethod
    def continue_chat(self, prompt: str):
        pass

    @abstractmethod
    def open_chat(self, step_id) -> None:
        pass

    @abstractmethod
    def close_chat(self) -> None:
        pass

    @abstractmethod
    def set_body(self, new_body: str) -> None:
        pass
