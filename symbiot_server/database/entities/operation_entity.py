import uuid

from database_provider import db


class OperationEntity(db.Model):
    __tablename__ = 'operations'
    id = db.Column(
        db.String,
        primary_key=True)
    wish = db.Column(db.Text)
    nord_star = db.Column(db.Text)
    leaf_summary_status = db.Column(db.Text, nullable=True)
    status = db.Column(db.String)
    name = db.Column(db.String)
    body = db.Column(db.Text)
    records = db.relationship(
        "RecordEntity", backref="operations", lazy=False)

    # noinspection PyMissingConstructor
    def __init__(self, wish, name="untitled", body="", id_=None,
                 nord_star=None, status="CREATION_STARTED",
                 leaf_summary_status=None, records=None):
        self.leaf_summary_status = leaf_summary_status
        self.id = str(uuid.uuid4()) if id_ is None else id_
        self.name = name
        self._records = []
        self.wish = wish
        self.nord_star = wish if nord_star is None else nord_star
        self.status = status
        self.body = body
        self.records = [] if records is None else records
