from flask_sqlalchemy import SQLAlchemy
from injector import inject

from symbiot_server.database.converters.client_converter import ClientConverter
from symbiot_server.database.entities.gpt_client_entity import GPTClientEntity
from symbiot_server.database.repositories.symbiot_repository import SymbiotRepository


class GPTClientRepository(SymbiotRepository):
    @inject
    def __init__(self, db: SQLAlchemy, client_converter: ClientConverter):
        super().__init__(db, GPTClientEntity, client_converter)
