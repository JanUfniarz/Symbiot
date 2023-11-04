from symbiot_core.connection.object_connector import ObjectConnector
from symbiot_lib.objects.step_record import StepRecord


class ChatHandler:

    # noinspection PyTypeChecker
    def __init__(self, object_connector: ObjectConnector):
        self.server = object_connector
        self._active_step: StepRecord = None

    def open_chat(self, step_id):
        self._active_step = self.server.get_record_by_id(step_id)

    def close_chat(self):
        print(self._active_step.current_status)
        self.server.put_pickle(self._active_step,
                               path="operation/record")
        self._active_step = None

    def continue_chat(self, prompt: str):
        step = self._active_step

        if not step:
            # TODO: implement
            raise NotImplementedError("no active step")
        step.add_entry(
            "user", prompt
        ).add_entry(
            "assistant", step.client.chat(prompt))
        return step.body
