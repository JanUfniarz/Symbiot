class Record:
    _converter = None

    def __init__(self, inputs, id_=None, previous=None, path=None,
                 outputs=None, body=None, status="", **ignored):
        self.id = id_
        self.previous = previous
        self.path = path
        self.inputs = inputs if inputs is not None else []
        self.outputs = outputs if outputs is not None else []
        self.body = body
        self.status = status

    @classmethod
    def inject_converter(cls, converter):
        cls._converter = converter

    @property
    def current_status(self) -> str:
        return self.status.split("/")[-1]

    def add_to_status(self, value):
        self.status += "/" + value

    def in_status(self, value) -> bool:
        return value in self.status.split("/")

    def to_dict(self):
        res = self.__dict__.copy()
        res["type"] = self._converter.type_to_string(self)
        res["inputs"] = list(map(
            lambda i: str(i),
            self.inputs))
        res["outputs"] = list(map(
            lambda o: str(o),
            self.outputs))
        if isinstance(res["previous"], Record):
            res["previous"] = res["previous"]["id_"]
        return res
