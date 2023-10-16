from database_provider import db
from operation_division.record.record import Record


class Operation(db.Model):
    __tablename__ = 'operations'
    id = db.Column(
        db.Integer,
        primary_key=True,)
    wish = db.Column(db.Text)
    nord_star = db.Column(db.Text)
    leaf_summary_status = db.Column(db.Text, nullable=True)
    status = db.Column(db.String)
    name = db.Column(db.String)
    body = db.Column(db.Text)
    _records = db.relationship(
        "RecordEntity", backref="operations", lazy=True)

    def __init__(self, wish, name="untitled", body=""):

        self.name = name
        self._records = []
        self.wish = wish
        self.nord_star = wish
        self.status = "CREATION_STARTED"
        self.body = body

    @property
    def records(self):
        records = [record.from_entity
                   for record in self._records]

        for record in records:
            if isinstance(record.previous, int):
                for it in records:
                    if record.previous == it.id:
                        record.previous = it

        return records

    def add_record(self, new: Record):
        self._records.append(new.to_entity)

    def to_dict(self):
        res = self.__dict__.copy()
        if "_sa_instance_state" in res:
            res.pop("_sa_instance_state")
        res["records"] = list(map(
            lambda r: r.to_dict(),
            self.records))
        return res
