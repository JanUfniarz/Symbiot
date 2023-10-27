from symbiot_core.connection.symbiot_connector import SymbiotConnector


class RecordConnector(SymbiotConnector):

    def __init__(self):
        super().__init__("record")

    def get_record(self, step_id):
        pass

    def save_record(self, step):
        pass
