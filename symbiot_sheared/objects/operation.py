from objects.record import Record
from objects.script_record import ScriptRecord
from objects.step_record import StepRecord


class Operation:
    def __init__(self, id_: str, wish: str, nord_star: str,
                 leaf_summary_status: str, status: str,
                 name: str, body: str, records: list[Record]):
        self.records: list[Record] = records
        self.body: str = body
        self.name: str = name
        self.status: str = status
        self.leaf_summary_status: str = leaf_summary_status
        self.nord_star: str = nord_star
        self.wish: str = wish
        self.id: str = id_

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

    def to_dict(self):
        res = self.__dict__.copy()
        res["records"] = list(map(
            lambda r: r.to_dict(),
            self.records))
        return res

    @staticmethod
    def join_records(records: list[Record]) -> list[Record]:
        for record in records:
            if isinstance(record.previous, int):
                for it in records:
                    if record.previous == it.id:
                        record.previous = it
        return records
