class Container:
    def __init__(self, inputs, previous=None, path=None,
                 outputs=None, body=None, status=""):
        self.previous = previous
        self.path = path
        self.inputs = inputs if inputs is not None else []
        self.outputs = outputs if outputs is not None else []
        self.body = body
        self.status = status
