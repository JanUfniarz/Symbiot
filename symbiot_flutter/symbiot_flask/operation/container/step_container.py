from .container import Container


class StepContainer(Container):
    def __init__(self, inputs, **kwargs):
        super().__init__(inputs, **kwargs)
