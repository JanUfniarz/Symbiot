from flask import Flask

from symbiot_server.config.divisions.action_division import ActionDivision
from symbiot_server.config.divisions.client_division import ClientDivision
from symbiot_server.config.database_provider import db
from symbiot_server.config.divisions.operation_division import OperationDivision
from symbiot_server.config.symbiot_starter import SymbiotStarter

app: Flask = Flask(__name__)

if __name__ == '__main__':
    symbiot: SymbiotStarter = SymbiotStarter().flask(app)\
        .sql_alchemy(
        db,
        'postgresql://postgres:postgres@localhost:5432/symbiot')\
        .divisions([
            OperationDivision(),
            ClientDivision(),
            ActionDivision()])\
        .mediator()\
        .listen_all().run()
