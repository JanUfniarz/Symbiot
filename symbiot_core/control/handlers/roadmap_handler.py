from injector import inject

from symbiot_core.connection.connectors.object_connector import ObjectConnector
from symbiot_core.control.handlers.chat_handler import ChatHandler


class RoadMapHandler(ChatHandler):
    @inject
    def __init__(self, object_connector: ObjectConnector):
        super().__init__(object_connector)



