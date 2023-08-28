from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY

from container import Container

db = SQLAlchemy()


class ContainerEntity(db.Model, Container):
    __tablename__ = 'containers'

    id = db.Column(db.Integer, primary_key=True)
    type_ = db.Column(db.Enum(
        "script", "step"
    ))
    previous = db.Column(db.Integer, nullable=True)
    path = db.Column(db.String, nullable=True)
    big_o = db.Column(db.Enum(
        "O(1)", "O(logN)", "O(N)", "O(NlogN)",
        "O(N^2)", "O(N^3)", "O(2^N)", "O(N!)",
        "API"
    ), nullable=True)
    inputs = db.Column(ARRAY(db.String))
    outputs = db.Column(ARRAY(db.String), nullable=True)
    body = db.Column(db.Text, nullable=True)
    status = db.Column(db.String)
    operation_id = db.Column(db.Integer, db.ForeignKey("operations.id"))

    def __init__(self, type_, inputs, path=None, previous=None, body=None):
        if type_ == "script" and path is not None:
            raise ValueError("Script need a path")

        if type_ == "step" and body is None:
            raise ValueError("Step need a body")

        self.previous = previous
        self.path = path
        self.inputs = inputs
        self.type_ = type_
        self.body = body
        self.status = ""
