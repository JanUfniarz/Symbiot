class Record:
    def __init__(self, inputs, id_=None, previous=None, path=None,
                 outputs=None, body=None, status="/", **ignored):
        self.id = id_
        self.previous = previous
        self.path = path
        self.inputs = inputs if inputs is not None else []
        self.outputs = outputs if outputs is not None else []
        self.body = body
        self.status = status

    def to_dict(self):
        import record_converter as converter
        res = self.__dict__.copy()
        res["type"] = converter.type_to_string(self)
        res["inputs"] = list(map(
            lambda i: i.__dict__.copy(),
            self.inputs))
        res["outputs"] = list(map(
            lambda o: o.__dict__.copy(),
            self.outputs))
        if isinstance(res["previous"], Record):
            res["previous"] = res["previous"]["id_"]
        return res


