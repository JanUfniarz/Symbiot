from flask import Flask
from injector import Injector

from client_division.client_division import ClientDivision
from client_division.keys_endpoint import KeysEndpoint
from database_provider import db
from mediator import Mediator
from operation_division.operation_endpoint import OperationEndpoint
from operation_division.operation_division import OperationDivision
from symbiot_division import SymbiotDivision

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:postgres@localhost:5432/symbiot'

db.init_app(app)

if __name__ == '__main__':
    """uncomment to rebuild database"""
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()

    SymbiotDivision.app = app
    SymbiotDivision.db = db

    symbiot = Injector([
        OperationDivision(),
        ClientDivision()])

    mediator = Mediator(symbiot)

    symbiot.get(OperationEndpoint).listen("/operation")
    symbiot.get(KeysEndpoint).listen("/key")

    app.run(debug=True)
