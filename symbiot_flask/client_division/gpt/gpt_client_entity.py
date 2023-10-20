import uuid

from sqlalchemy.dialects.postgresql import ARRAY

from client_division.gpt.gpt_client import GPTClient
from database_provider import db


class GPTClientEntity(db.Model):
    __tablename__ = 'gpt_clients'
    id = db.Column(
        db.String,
        primary_key=True)
    model = db.Column(db.String)
    temperature = db.Column(db.Float)
    n = db.Column(db.Integer)
    max_tokens = db.Column(db.Integer)
    system_prompts = db.Column(ARRAY(db.String))
    step_id = db.Column(db.String, db.ForeignKey("records.id"))

    def __init__(self, client: GPTClient):
        self.id = str(uuid.uuid4()) \
            if client.id is None else client.id
        self.model = client.model
        self.temperature = client.temperature
        self.n = client.n
        self.max_tokens = client.max_tokens

        self.system_prompts = [
            val["content"]
            for val in client.messages
            if val["role"] == "system"
        ]

    @property
    def from_entity(self) -> GPTClient:
        args = self.__dict__.copy()

        args["init_messages"] = [dict(
            role="system",
            content=prompt
        ) for prompt in args.pop("system_prompts")]

        if "_sa_instance_state" in args:
            args.pop("_sa_instance_state")

        return GPTClient(**args)
