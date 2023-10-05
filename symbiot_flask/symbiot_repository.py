from flask_sqlalchemy import SQLAlchemy


class SymbiotRepository:
    def __init__(self, database: SQLAlchemy, entity):
        self.db = database
        self._entity = entity

    def save(self, entity):
        self.db.session.merge(entity)
        self.db.session.commit()

    def get_all(self):
        return self.db.session.query(self._entity).all()
