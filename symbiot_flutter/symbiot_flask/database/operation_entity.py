from operation_dao import OperationDAO

db = OperationDAO().db


class Operation(db.Model):
    __tablename__ = 'operations'

    op_id = db.Column(
        db.Integer,
        primary_key=True,
    )

    wish = db.Column(db.Text)
    nord_star = db.Column(db.Text)
    leaf_summary_status = db.Column(db.Text)

    def __init__(self, wish, nord_star, links,
                 leaf_summary_status, steps, script_containers, body,):

        self.script_containers = script_containers
        self.leaf_summary_status = leaf_summary_status
        self.wish = wish
        self.nord_star = nord_star
        self.status = "CREATION_STARTED"
        self.steps = steps
        self.body = body
