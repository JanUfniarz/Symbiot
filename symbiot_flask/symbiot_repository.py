from flask_sqlalchemy import SQLAlchemy


class SymbiotRepository:
    def __init__(self, database: SQLAlchemy, entity):
        self._db = database
        self.entity = entity

    def save(self, entity):
        self._db.session.add(entity)
        self._db.session.commit()

    def get_all(self):
        return self._db.session.query(self.entity).all()
