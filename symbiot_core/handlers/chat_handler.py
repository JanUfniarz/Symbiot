from symbiot_core.connection.record_connector import RecordConnector
from symbiot_lib.objects.step_record import StepRecord


class ChatHandler:

    # noinspection PyTypeChecker
    def __init__(self, step_connector: RecordConnector):
        self.step_connector = step_connector
        self._active_step: StepRecord = None

    def open_chat(self, step_id):
        self._active_step = self.step_connector.get_record(step_id)

    def close_chat(self):
        self.step_connector.save_record(self._active_step)
        self._active_step = None

    def continue_chat(self, prompt: str):
        step = self._active_step

        if not step:
            # TODO: implement
            raise NotImplementedError("no active step")
        response = step.client.chat(prompt)
        step.add_entry(prompt, response)
        return step.body
