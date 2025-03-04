from sqlalchemy.dialects.postgresql import ARRAY

from symbiot_lib.objects.record import Record
from symbiot_server.config.database_provider import db


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
    agent = db.Column(db.LargeBinary, nullable=True)

    def __init__(self, type_, inputs, big_o=None,  **kwargs):
        super().__init__(inputs=inputs, **kwargs)
        self.type_ = type_
        self.big_o = big_o

    @property
    def type_str(self) -> str:
        return "entity"
