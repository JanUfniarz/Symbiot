import sys

from flask import Flask

from symbiot_core.config.core_division import CoreDivision
from symbiot_core.connection.pickle_connector import PickleConnector
from symbiot_core.endpoints.chat_endpoint import ChatEndpoint
from symbiot_core.endpoints.keys_endpoint import KeysEndpoint
from symbiot_core.endpoints.main_endpoint import MainEndpoint
from symbiot_lib.components.symbiot_starter import SymbiotStarter

app: Flask = Flask(__name__)

if __name__ == '__main__':
    symbiot_core: SymbiotStarter = SymbiotStarter(dict(
        main=MainEndpoint,
        chat=ChatEndpoint,
        key=KeysEndpoint
    )).flask(app).divisions([
        CoreDivision()
    ]).listen_all()

    # docker_mode: bool = '--docker' in sys.argv
    # print(docker_mode)
    #
    # symbiot_core(PickleConnector).docker_mode = docker_mode
    #
    # print(symbiot_core(PickleConnector).docker_mode)

    symbiot_core.run(debug=True, host='0.0.0.0', port=5001)
