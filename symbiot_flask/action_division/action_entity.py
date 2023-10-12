from database_provider import db


class Action(db.Model):
    __tablename__ = 'actions'
    id = db.Column(
        db.Integer,
        primary_key=True)
    command = db.Column(db.String)
    status = db.Column(db.String)
    output = db.Column(db.String)
    operation_id = db.Column(db.Integer, db.ForeignKey("operations.id"))

    def __init__(self, operation_id: int,
                 command: str = None,
                 status: str = None,
                 output: str = None):
        self.output = output
        self.status = status
        self.command = command
        self.operation_id = operation_id
