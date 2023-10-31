from flask import Flask

from symbiot_server.config.divisions.action_division import ActionDivision
from symbiot_server.config.divisions.client_division import ClientDivision
from symbiot_server.config.database_provider import db
from symbiot_server.config.divisions.operation_division import OperationDivision
from symbiot_server.config.server_starter import ServerStarter

app: Flask = Flask(__name__)

if __name__ == '__main__':
    symbiot_server: ServerStarter = ServerStarter().flask(
        app
    ).sql_alchemy(
        db,
        'postgresql://postgres:postgres@localhost:5432/symbiot'
    ).divisions([
            OperationDivision(),
            ClientDivision(),
            ActionDivision()
    ]).mediator().listen_all().run(debug=True, port=5000)
