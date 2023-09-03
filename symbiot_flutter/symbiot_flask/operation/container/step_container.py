from datetime import datetime

from .container import Container


class StepContainer(Container):
    def __init__(self, inputs, **kwargs):
        super().__init__(inputs, **kwargs)

    def add_entry(self, prompt, response):
        self.body += f"<@entry>{datetime.now()}" \
                     f"<@time>{prompt}<@res>{response}"
