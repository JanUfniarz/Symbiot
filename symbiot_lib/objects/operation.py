import uuid

from symbiot_lib.objects.record import Record
from symbiot_lib.objects.script_record import ScriptRecord
from symbiot_lib.objects.step_record import StepRecord


class Operation:
    def __init__(self, id_: str = None,
                 wish: str = None, nord_star: str = None,
                 leaf_summary_status: str = None, status: str = None,
                 name: str = None, body: str = None, records: list[Record] = None):
        self._records: list[Record] = records
        self.body: str = body
        self.name: str = name
        self.status: str = status
        self.leaf_summary_status: str = leaf_summary_status
        self.nord_star: str = nord_star
        self.wish: str = wish
        self.id: str = str(uuid.uuid4()) if id_ is None else id_

    @property
    def records(self) -> list[Record]:
        return self._records.copy()

    def add_or_update_record(self, record: Record) -> None:
        for it, record_ in enumerate(self._records):
            if record.id == record_.id:
                self._records[it] = record
                return
        self._records.append(record)

    def remove_record(self, record: Record) -> None:
        if record in self._records:
            self._records.remove(record)

    def from_dict(self, data: dict):
        def record_from_dict(record_data: dict):
            match record_data.pop("type"):
                case "step": return StepRecord(record_data.pop("inputs"), **record_data)
                case "script": return ScriptRecord(record_data.pop("inputs"), **record_data)
            return None

        data["records"] = self.join_records(list(map(
            lambda r: record_from_dict(r),
            data["records"])))

        return Operation(*data)

    @property
    def serialized(self) -> dict:
        res = self.__dict__.copy()
        res["records"] = list(map(
            lambda r: r.serialized,
            res.pop("_records")))
        return res

    @staticmethod
    def join_records(records: list[Record]) -> list[Record]:
        for record in records:
            if isinstance(record.previous, int):
                for it in records:
                    if record.previous == it.id:
                        record.previous = it
        return records
