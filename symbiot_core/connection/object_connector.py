from symbiot_core.connection.pickle_connector import PickleConnector, endpoint
from symbiot_lib.objects.gpt_client import GPTClient
from symbiot_lib.objects.operation import Operation
from symbiot_lib.objects.record import Record


class ObjectConnector(PickleConnector):

    def __init__(self):
        super().__init__()

    @endpoint("client")
    def get_client_by_name(self, name: str) -> GPTClient:
        return self.get_pickle(dict(
            by="name",
            content=name))

    @endpoint("operation")
    def get_operation_by_record(self, record: Record) -> Operation:
        return self.get_pickle(dict(
            by="record_id",
            content=record.id))

    @endpoint("operation/record")
    def get_record_by_id(self, record_id: str) -> Record:
        return self.get_pickle(dict(
            by="id",
            content=record_id))
