from .container import Container


class ScriptContainer(Container):
    def __init__(self, inputs, big_o=None,  **kwargs):
        super().__init__(inputs, **kwargs)
        self.big_o = big_o
