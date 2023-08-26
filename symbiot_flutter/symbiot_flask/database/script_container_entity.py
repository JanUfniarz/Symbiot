from sqlalchemy.dialects.postgresql import ARRAY

from operation_dao import OperationDAO

db = OperationDAO().db


class ScriptContainer(OperationDAO().db):

    __tablename__ = 'script_containers'

    # + -> next | - -> previous
    branches = (ARRAY(db.Integer()))

    def __init__(self, branches, path, big_o_notation, status, ):
        self.branches = branches
