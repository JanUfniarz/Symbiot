from sqlalchemy.dialects.postgresql import ARRAY

from database_provider import db
from objects.record import Record


class RecordEntity(Record, db.Model):
    __tablename__ = 'records'

    id = db.Column(
        db.String,
        primary_key=True)

    type_ = db.Column(db.Enum(
        "script", "step", name="type"))

    previous = db.Column(db.Integer, nullable=True)
    path = db.Column(db.String, nullable=True)
    big_o = db.Column(db.Enum(
        "O(1)", "O(logN)", "O(N)", "O(NlogN)",
        "O(N^2)", "O(N^3)", "O(2^N)", "O(N!)",
        "API", name="big_o"
    ), nullable=True)

    inputs = db.Column(ARRAY(db.String))
    outputs = db.Column(ARRAY(db.String), nullable=True)
    body = db.Column(db.Text, nullable=True)
    status = db.Column(db.String)
    operation_id = db.Column(db.String, db.ForeignKey("operations.id"))
    client = db.Column(db.String)

    def __init__(self, type_, inputs, big_o=None,  **kwargs):
        super().__init__(inputs=inputs, **kwargs)
        self.type_ = type_
        self.big_o = big_o

    @property
    def type_str(self):
        return "entity"
