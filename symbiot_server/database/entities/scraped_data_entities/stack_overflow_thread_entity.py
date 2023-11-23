import uuid

from symbiot_server.config.database_provider import db
from symbiot_server.database.entities.scraped_data_entities.stack_overflow_post_entity import StackOverflowPostEntity


class StackOverflowThreadEntity(db.Model):
    __tablename__ = 'threads'
    id = db.Column(
        db.String,
        primary_key=True)
    title = db.Column(db.String)
    posts = db.relationship(
        "StackOverflowPostEntity", backref="threads", lazy=False)

    def __init__(self, data: dict):
        self.id: str = str(uuid.uuid4())
        self.title: str = data["thread_title"]
        self.posts: list[StackOverflowPostEntity] = [StackOverflowPostEntity(
            "question",
            data["question"]["content"],
            data["question"]["votes"])] + [
            StackOverflowPostEntity(
                "answer",
                el["content"],
                el["votes"])
            for el in data["answers"]]
