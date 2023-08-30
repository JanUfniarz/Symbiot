from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY

from .container import Container

db = SQLAlchemy()


class ContainerEntity(db.Model, Container):
    __tablename__ = 'containers'

    id = db.Column(db.Integer, primary_key=True)
    type_ = db.Column(db.Enum(
        "script", "step", name="type"
    ))
    previous = db.Column(db.Integer, nullable=True)
    path = db.Column(db.String, nullable=True)
    big_o = db.Column(db.Enum(
        "O(1)", "O(logN)", "O(N)", "O(NlogN)",
        "O(N^2)", "O(N^3)", "O(2^N)", "O(N!)",
        "API", name="big_o"
    ), nullable=True)
    inputs = db.Column(ARRAY(db.String))
    outputs = db.Column(ARRAY(db.String))
    body = db.Column(db.Text, nullable=True)
    status = db.Column(db.String)
    operation_id = db.Column(db.Integer, db.ForeignKey("operations.id"))

    def __init__(self, type_, inputs, big_o=None,  **kwargs):
        if type_ == "script" and kwargs.get("path", None) is None:
            raise ValueError("Script need a path")

        if type_ == "step" and kwargs.get("body", None) is None:
            raise ValueError("Step need a body")

        super().__init__(inputs=inputs, **kwargs)
        self.type_ = type_
        self.big_o = big_o
