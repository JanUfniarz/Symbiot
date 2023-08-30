from operation.container.container_entity import db

db = db


class Operation(db.Model):
    __tablename__ = 'operations'

    id = db.Column(
        db.Integer,
        primary_key=True,)
    wish = db.Column(db.Text)
    nord_star = db.Column(db.Text)
    leaf_summary_status = db.Column(db.Text)
    status = db.Column(db.String)
    name = db.Column(db.String)
    body = db.Column(db.Text)
    containers = db.relationship(
        "ContainerEntity", backref="operations", lazy=True)

    def __init__(self, name, wish, containers, body,):

        self.name = name
        self.containers = containers
        self.wish = wish
        self.nord_star = wish
        self.status = "CREATION_STARTED"
        self.body = body
