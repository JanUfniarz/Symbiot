import uuid

from symbiot_server.config.database_provider import db


class StackOverflowPostEntity(db.Model):
    __tablename__ = 'posts'
    id = db.Column(
        db.String,
        primary_key=True)
    content = db.Column(db.String)
    votes = db.Column(db.Integer)
    type_ = db.Column(db.Enum(
        "question", "answer", name="type"))
    thread_id = db.Column(db.String, db.ForeignKey("threads.id"))

    def __init__(self, type_: str, content: str, votes: int):
        self.id: str = str(uuid.uuid4())
        self.votes: int = votes
        self.content: str = content
        self.type_: str = type_
