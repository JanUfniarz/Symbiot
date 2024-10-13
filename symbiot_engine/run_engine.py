from flask import Flask

from symbiot_engine.config.engine_division import EngineDivision
from symbiot_engine.connection.endpoints.chat_endpoint import ChatEndpoint
from symbiot_engine.connection.endpoints.keys_endpoint import KeysEndpoint
from symbiot_engine.connection.endpoints.main_endpoint import MainEndpoint
from symbiot_lib.components.symbiot_starter import SymbiotStarter

app: Flask = Flask(__name__)

if __name__ == '__main__':
    symbiot_core: SymbiotStarter = SymbiotStarter(dict(
        main=MainEndpoint,
        chat=ChatEndpoint,
        key=KeysEndpoint
    )).flask(app).divisions([
        EngineDivision()
    ]).listen_all().run(debug=True, host='0.0.0.0', port=5001)
