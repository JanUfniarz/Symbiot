import uuid
from abc import abstractmethod


class Record:

    def __init__(self, inputs, id_=None, previous=None, path=None,
                 outputs=None, body="", status="", client=None, **ignored):
        self.client = client
        self.id: str = str(uuid.uuid4()) if id_ is None else id_
        self.previous = previous
        self.path: str = path
        self.inputs: list = inputs if inputs is not None else []
        self.outputs: list = outputs if outputs is not None else []
        self.body: str = body
        self.status: str = status

    @property
    def current_status(self) -> str:
        return self.status.split("/")[-1]

    @abstractmethod
    def type_str(self):
        pass

    def add_to_status(self, value):
        self.status += "/" + value

    def in_status(self, value) -> bool:
        return value in self.status.split("/")

    @property
    def to_dict(self) -> dict:
        res = self.__dict__.copy()
        res["type"] = self.type_str()
        if isinstance(res["previous"], Record):
            res["previous"] = self.previous.id
        return res
