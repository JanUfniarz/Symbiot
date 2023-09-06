from injector import inject

from .gpt.gpt_connector import GPTConnector


class CreativeService:
    @inject
    def __init__(self, gtp_connector: GPTConnector):
        self.gpt = gtp_connector

