from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


class SymbiotRepository:
    def __init__(self, database: SQLAlchemy, entity, base_converter):
        self.base_converter = base_converter
        self.db = database
        self._entity = entity

    def save(self, object_):
        self.db.session.merge(self.base_converter.to_entity(object_))
        self.db.session.commit()

    def get_all(self) -> list:
        return list(map(lambda entity: self.base_converter.from_entity(entity),
                        self.db.session.query(self._entity).all()))

    def execute(self, query: str):
        self.db.session.execute(text(query))
        self.db.session.commit()
