from datetime import datetime

from symbiot_lib.objects.record import Record


class StepRecord(Record):
    @property
    def type_str(self):
        return "step"

    def __init__(self, inputs, **kwargs):
        super().__init__(inputs, **kwargs)

    def add_entry(self, prompt, response):
        def now() -> str:
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.body += f"<@entry>{now()}<@time>{prompt}<@res>{response}"
