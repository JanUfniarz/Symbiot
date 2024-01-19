import sys

from flask import Flask

from symbiot_server.config.divisions.client_division import ClientDivision
from symbiot_server.config.database_provider import db
from symbiot_server.config.divisions.operation_division import OperationDivision
from symbiot_server.config.server_starter import ServerStarter

app: Flask = Flask(__name__)

if __name__ == '__main__':
    db_host: str = 'symbiot-database-1' \
        if '--docker' in sys.argv else 'localhost'

    symbiot_server: ServerStarter = ServerStarter().flask(
        app
    ).sql_alchemy(
        db,
        f'postgresql://postgres:postgres@{db_host}:5432/symbiot'
    ).divisions([
            OperationDivision(),
            ClientDivision(),
    ]).mediator().listen_all().run(debug=True, host='0.0.0.0', port=5000)
