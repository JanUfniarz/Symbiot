from datetime import datetime

from objects.gpt_client import GPTClient
from objects.record import Record


class StepRecord(Record):
    @property
    def type_str(self):
        return "step"

    def __init__(self, inputs,
                 client: GPTClient = None, **kwargs):
        super().__init__(inputs, **kwargs)
        self.client: GPTClient = client

    def add_entry(self, prompt, response):
        def now() -> str:
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.body += f"<@entry>{now()}<@time>{prompt}<@res>{response}"
