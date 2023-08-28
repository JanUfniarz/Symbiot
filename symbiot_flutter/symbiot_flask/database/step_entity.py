from sqlalchemy.dialects.postgresql import ARRAY

from operation_dao import OperationDAO

db = OperationDAO().db


class Step(db.Model):

    __tablename__ = 'steps'

    # + -> next | - -> previous
    branches = (ARRAY(db.Integer())) # TODO: poprzedni id
    level = (ARRAY(db.Integer()))

    def __init__(self, branches, level):
        self.branches = branches
        self.level = level
