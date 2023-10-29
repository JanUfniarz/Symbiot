from injector import inject

from symbiot_core.connection.object_connector import ObjectConnector
from symbiot_core.connection.pickle_connector import endpoint
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
        operation.add_record(step)

        self.server.put_pickle(operation,
                               path="operation")

        self._active_step = step
        self.continue_chat(wish)
        self.close_chat()

    def assign_nord_star(self, nord_star, name):
        step = self._active_step
        step.inputs.append(name)
        step.outputs.append(nord_star)
        step.add_to_status("done")

        operation = self.server.get_operation_by_record(step)

        operation.name = step.inputs[0]
        operation.nord_star = step.outputs[0]
        self.server.put_pickle(operation, path="operation")
