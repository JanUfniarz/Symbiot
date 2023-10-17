from flask_sqlalchemy import SQLAlchemy


class SymbiotRepository:
    def __init__(self, database: SQLAlchemy, entity):
        self.db = database
        self._entity = entity

    def save(self, entity):
        entity_ = entity
        self.db.session.merge(entity_)
        self.db.session.commit()
        return entity_

    def get_all(self):
        return self.db.session.query(self._entity).all()
