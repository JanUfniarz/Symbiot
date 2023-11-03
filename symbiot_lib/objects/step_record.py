import json
from datetime import datetime

from symbiot_lib.objects.record import Record


class StepRecord(Record):
    @property
    def type_str(self):
        return "step"

    def __init__(self, inputs, **kwargs):
        super().__init__(inputs, **kwargs)

    def add_entry(self, role: str, content: str):
        """
        Adds one entry to the step.

        :param role: enumerate: 'user', 'assistant', 'server', 'error'
        :param content: content of the message

        chain method (return self)
        """
        self.body += ("<@entry>" +
                      json.dumps(dict(
                          time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          role=role,
                          content=content)))
        return self
