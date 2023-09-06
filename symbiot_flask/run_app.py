from flask import Flask
from injector import Injector

from creative_division.creative_division import CreativeDivision
from operation_division.operation_controller import OperationController
from operation_division.operation_division import OperationDivision
from operation_division.operation_entity import db as operation_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:postgres@localhost:5432/symbiot'

operation_db.init_app(app)

if __name__ == '__main__':
    # with app.app_context():
    #     operation_db.drop_all()
    #     operation_db.create_all()

    # creative_division = CreativeService(
    #     GPTConnector()),
    #
    # operation_division = OperationController(
    #     app,
    #     "/operation",
    #     OperationService(
    #         PSCommandGenerator(),
    #         OperationDAO(operation_db)))
    #
    # operation_division.service\
    #     .wire_creative_division(creative_division)

    symbiot = Injector([
        OperationDivision(app, operation_db),
        CreativeDivision()
    ])

    symbiot.get(OperationController).listen("/operation")

    app.run(debug=True)
