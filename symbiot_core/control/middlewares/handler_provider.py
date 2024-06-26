from injector import inject

from symbiot_core.control.handler_interface import HandlerInterface
from symbiot_core.control.handlers.calibration_handler import CalibrationHandler
from symbiot_core.control.handlers.chat_handler import ChatHandler
from symbiot_lib.objects.step_record import StepRecord


class HandlerProvider(HandlerInterface):
    @inject
    def __init__(self, calibration_handler: CalibrationHandler):
        self._handlers: dict[str, ChatHandler] = dict(
            calibration=calibration_handler
        )
        # noinspection PyTypeChecker
        self._active_handler: ChatHandler = None

    def continue_chat(self, prompt: str):
        return self._check_and_reload(self._handler().continue_chat(prompt))

    def open_chat(self, status, step_id):
        return self._handler(status).open_chat(step_id)

    def close_chat(self):
        return self._handler().close_chat()

    def set_body(self, new_body: str) -> None:
        return self._handler().set_body(new_body)

    def _handler(self, status: str = None) -> ChatHandler:
        def set_handler(status_):
            for tag in [tag for tag in status_.split("/") if tag.startswith("TO=")]:
                if tag.replace("TO=", "") in self._handlers:
                    self._active_handler = self._handlers[tag.replace("TO=", "")]

        if status is not None:
            set_handler(status)
        if self._active_handler is None:
            raise ValueError("No active handler, provide proper status")
        return self._active_handler

    def _check_and_reload(self, body):
        step: StepRecord = self._active_handler.active_step
        status: str = step.current_status

        if not status.startswith("TO="):
            return body, False

        new_handler = self._handler(status)
        new_handler.create(step)
        return body, True

        #
        # - sprawdzić czy ma przeładować
        # - na podastawie statusu dobrać kolejny handler
        #
        # odpalić create i włożyć active_step
        #
        #
        # ! tam utworzyć nowy step i zapisać do backendu
        #
        # zwrócić dane do response a w nich informację o potrzebnym switchu
        #
        # ! przetworzyć na frontendzie i backendzie
        #
