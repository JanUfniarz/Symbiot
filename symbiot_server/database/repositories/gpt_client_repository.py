from flask_sqlalchemy import SQLAlchemy
from injector import inject

from client_division.client_converter import ClientConverter
from client_division.gpt.gpt_client_entity import GPTClientEntity
from symbiot_repository import SymbiotRepository


class GPTClientRepository(SymbiotRepository):
    @inject
    def __init__(self, db: SQLAlchemy, client_converter: ClientConverter):
        super().__init__(db, GPTClientEntity, client_converter)
