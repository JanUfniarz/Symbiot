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

    def is_available(self, id_: str, table_name: str = None) -> bool:
        # language=POSTGRES-PSQL
        return self.db.session.execute(text(f"""
            SELECT id 
            FROM {table_name if table_name else self._entity.__tablename__} 
            WHERE id = '{id_}';
        """)).fetchone() is not None

    def update_value(self, id_, to_change, value) -> None:
        # language=POSTGRES-PSQL
        self.db.session.execute(text(f"""
            UPDATE {self._entity.__tablename__} 
            SET {to_change} = '{value}'
            WHERE id = '{id_}';
        """))
        self.db.session.commit()
