from datetime import datetime

from .record import Record


class StepRecord(Record):
    def __init__(self, inputs, client=None, **kwargs):
        super().__init__(inputs, **kwargs)
        self.client = client

    def add_entry(self, prompt, response):
        def now() -> str:
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.body += f"<@entry>{now()}<@time>{prompt}<@res>{response}"
