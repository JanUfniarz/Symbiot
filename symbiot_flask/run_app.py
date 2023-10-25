from flask import Flask

from action_division.action_division import ActionDivision
from client_division.client_division import ClientDivision
from database_provider import db
from operation_division.operation_division import OperationDivision
from symbiot_starter import SymbiotStarter

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
