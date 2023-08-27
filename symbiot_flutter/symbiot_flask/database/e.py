# import os
# import sys
#
#
# sys.path.append(
#     os.path.abspath(
#         os.path.join(
#             os.path.dirname(__file__),
#             '..')))
#
# from run_app import db

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class E(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(255))

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
