from injector import inject

from symbiot_core.connection.connectors.object_connector import ObjectConnector
from symbiot_core.control.handlers.chat_handler import ChatHandler
from symbiot_lib.objects.operation import Operation


class CalibrationHandler(ChatHandler):

    @inject
    def __init__(self, object_connector: ObjectConnector):
        super().__init__(object_connector)

    def create(self, wish, status="calibration", previous=None):
        # noinspection PyTypeChecker
        operation = Operation(
            None, wish, wish,
            "", "NEW",
            "unnamed", "", [])

        step = self.new_step(status, previous)
        operation.add_or_update_record(step)

        self.server.post_pickle(operation,
                                path="operation")

        self.active_step = step
        self.continue_chat(wish)
        self.close_chat()

    def continue_chat(self, prompt: str) -> str:  # * overwrite
        self.active_step.client.tool_kit.func = self.assign_nord_star
        res = super().continue_chat(prompt)
        self.active_step.client.tool_kit.func = None
        return res

    def assign_nord_star(self, nord_star, name):  # * callback method
        step = self.active_step
        step.inputs.append(name)
        step.outputs.append(nord_star)
        step.add_to_status("ns_generated")
