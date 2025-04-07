from symbiot_engine.control.handlers.chat_handler import ChatHandler
from symbiot_lib.objects.step_record import StepRecord


class SplitHandler(ChatHandler):
    def create(self, operation_id) -> None:
        operation = self.server.get_pickle(dict(
            by="id",
            content=operation_id
        ))
        step = StepRecord([], agent=self.server.get_agent_by_name("splitter"))
        operation.add_or_update_record(step)

        self.active_step = step
