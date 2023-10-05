from database_provider import db


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
    _converter = None

    def __init__(self, wish, name="untitled", body=""):

        self.name = name
        self._records = []
        self.wish = wish
        self.nord_star = wish
        self.status = "CREATION_STARTED"
        self.body = body

    @classmethod
    def inject_converter(cls, converter):
        cls._converter = converter

    @property
    def records(self):
        records = [self._converter.from_entity(entity)
                   for entity in self._records]

        for record in records:
            if isinstance(record.previous, int):
                for it in records:
                    if record.previous == it.id:
                        record.previous = it.id

        return records

    def add_record(self, new):
        self._records.append(self._converter.to_entity(new))

    def to_dict(self):
        res = self.__dict__.copy()
        if "_sa_instance_state" in res:
            res.pop("_sa_instance_state")
        res["records"] = list(map(
            lambda r: r.to_dict(),
            self.records))
        return res
