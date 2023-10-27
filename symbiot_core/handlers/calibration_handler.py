from injector import inject

from symbiot_core.handlers.chat_handler import ChatHandler
from symbiot_core.connection.client_connector import ClientConnector
from symbiot_core.connection.operation_connector import OperationConnector
from symbiot_core.connection.record_connector import RecordConnector
from symbiot_lib.objects.operation import Operation
from symbiot_lib.objects.step_record import StepRecord


class CalibrationHandler(ChatHandler):

    @inject
    def __init__(self, client_connector: ClientConnector,
                 step_connector: RecordConnector,
                 operation_connector: OperationConnector):
        super().__init__(step_connector)
        self.operation_connector = operation_connector
        self.client_connector = client_connector

    def create(self, wish):
        # noinspection PyTypeChecker
        operation = Operation(
            None, wish, wish,
            "", "NEW",
            "unnamed", "", [])

        step = StepRecord([], client=self.client_connector.calibrator())
        step.add_to_status("calibration")
        step.client.tool_kit.func = self.assign_nord_star

        self._active_step = step
        self.continue_chat(wish)
        self.close_chat()

        operation.add_record(step)


    def assign_nord_star(self, nord_star, name):
        step = self._active_step
        step.inputs.append(name)
        step.outputs.append(nord_star)
        step.add_to_status("done")

        operation = self.operation_connector.get_by_step(step)

        operation.name = step.inputs[0]
        operation.nord_star = step.outputs[0]
