from symbiot_lib.objects.record import Record


class ScriptRecord(Record):
    @property
    def type_str(self):
        return "script"

    def __init__(self, inputs, big_o=None,  **kwargs):
        super().__init__(inputs, **kwargs)
        self.big_o = big_o
