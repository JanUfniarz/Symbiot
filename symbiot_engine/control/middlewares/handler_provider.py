from injector import inject

from symbiot_engine.control.handler_interface import HandlerInterface
from symbiot_engine.control.handlers.calibration_handler import CalibrationHandler
from symbiot_engine.control.handlers.chat_handler import ChatHandler
from symbiot_lib.objects.step_record import StepRecord


class HandlerProvider(HandlerInterface):
    @inject
    def __init__(self, calibration_handler: CalibrationHandler):
        self._handlers: dict[str, ChatHandler] = dict(
            calibration=calibration_handler
        )
        # noinspection PyTypeChecker
        self._active_handler: ChatHandler = None

    def continue_chat(self, prompt: str) -> tuple[str, bool]:
        return self._check_and_reload(self._handler().continue_chat(prompt))

    def open_chat(self, status: str, step_id: str) -> None:
        return self._handler(status).open_chat(step_id)

    def close_chat(self) -> None:
        return self._handler().close_chat()

    def set_body(self, new_body: str) -> None:
        return self._handler().set_body(new_body)

    def _handler(self, status: str = None) -> ChatHandler:

        if status is not None:
            for tag in [tag for tag in status.split("/") if tag.startswith("TO=")]:
                if tag.replace("TO=", "") in self._handlers:
                    self._active_handler = self._handlers[tag.replace("TO=", "")]

        if self._active_handler is None:
            raise ValueError("No active handler, provide proper status")
        return self._active_handler

    def _check_and_reload(self, body: str) -> tuple[str, bool]:
        step: StepRecord = self._active_handler.active_step
        status: str = step.current_status

        if not status.startswith("TO="):
            return body, False

        new_handler = self._handler(status)
        new_handler.create(step)
        return body, True
