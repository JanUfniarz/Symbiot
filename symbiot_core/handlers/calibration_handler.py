from injector import inject

from symbiot_core.connection.object_connector import ObjectConnector
from symbiot_core.handlers.chat_handler import ChatHandler
from symbiot_lib.objects.operation import Operation
from symbiot_lib.objects.step_record import StepRecord


class CalibrationHandler(ChatHandler):

    @inject
    def __init__(self, object_connector: ObjectConnector):
        super().__init__(object_connector)

    def create(self, wish):
        # noinspection PyTypeChecker
        operation = Operation(
            None, wish, wish,
            "", "NEW",
            "unnamed", "", [])

        step = StepRecord([], client=self.server.get_client_by_name("calibrator"))
        step.add_to_status("calibration")
        step.client.tool_kit.func = self.assign_nord_star
        operation.add_or_update_record(step)

        self.server.put_pickle(operation,
                               path="operation")

        self._active_step = step
        self.continue_chat(wish)
        self.close_chat()

    def open_chat(self, step_id):  # * overwrite
        # ! I'm not sure why it is necessary
        super().open_chat(step_id)
        self._active_step.client.tool_kit.func = self.assign_nord_star

    def assign_nord_star(self, nord_star, name):  # * callback method
        print("nord_star assigned")
        step = self._active_step
        step.inputs.append(name)
        step.outputs.append(nord_star)
        step.add_to_status("ns_generated")
        print(self._active_step.current_status)
