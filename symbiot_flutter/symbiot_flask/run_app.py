from flask import Flask

from components.ps_command_generator import PSCommandGenerator
from creative_division.creative_service import CreativeService

from operation.operation_controller import OperationController
from operation.operation_dao import OperationDAO
from operation.operation_entity import db as operation_db
from operation.operation_service import OperationService
from creative_division.gpt.gpt_connector import GPTConnector

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:postgres@localhost:5432/symbiot'

operation_db.init_app(app)

if __name__ == '__main__':
    # with app.app_context():
    #     operation_db.drop_all()
    #     operation_db.create_all()

    creative_division = CreativeService(
        GPTConnector()),

    operation_division = OperationController(
        app,
        "/operation",
        OperationService(
            PSCommandGenerator(),
            OperationDAO(operation_db)))

    operation_division.service\
        .wire_creative_division(creative_division)

    app.run(debug=True)
