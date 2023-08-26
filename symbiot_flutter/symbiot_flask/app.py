from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from operation.operation_controller import OperationController
from operation.operation_service import OperationService
from api.gpt_connector import GPTConnector
from components.ps_command_generator import PSCommandGenerator
from database.operation_dao import OperationDAO

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:postgres@localhost:5432/symbiot'
db = SQLAlchemy(app)

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()

    dao = OperationDAO(db)

    operation_division = OperationController(
        app,
        "/operation",
        OperationService(
            GPTConnector(),
            PSCommandGenerator(),
            dao
        )
    )

    app.run(debug=True)
