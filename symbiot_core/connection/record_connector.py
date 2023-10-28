from symbiot_core.connection.pickle_connector import PickleConnector


class RecordConnector(PickleConnector):

    def __init__(self):
        super().__init__("record")

    def get_record(self, step_id):
        pass

    def save_record(self, step):
        pass
