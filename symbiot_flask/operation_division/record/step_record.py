from datetime import datetime

from .record import Record


class StepRecord(Record):
    def __init__(self, inputs, client=None, **kwargs):
        super().__init__(inputs, **kwargs)
        self.client = client

    def add_entry(self, prompt, response):
        self.body += f"<@entry>{datetime.now()}" \
                     f"<@time>{prompt}<@res>{response}"
