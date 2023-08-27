from flask import Flask

from api.gpt_connector import GPTConnector
from components.ps_command_generator import PSCommandGenerator
from database.e import db as e_db
from database.operation_dao import OperationDAO
from operation.operation_controller import OperationController
from operation.operation_service import OperationService

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:postgres@localhost:5432/symbiot'
e_db.init_app(app)

if __name__ == '__main__':
    # with app.app_context():
    #     e_db.drop_all()
    #     e_db.create_all()

    operation_division = OperationController(
        app,
        "/operation",
        OperationService(
            GPTConnector(),
            PSCommandGenerator(),
            OperationDAO(e_db)
        )
    )

    app.run(debug=True)
