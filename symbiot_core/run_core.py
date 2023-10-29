from flask import Flask

from symbiot_core.config.core_division import CoreDivision
from symbiot_core.endpoints.chat_endpoint import ChatEndpoint
from symbiot_core.endpoints.main_endpoint import MainEndpoint
from symbiot_lib.components.symbiot_starter import SymbiotStarter

app: Flask = Flask(__name__)

if __name__ == '__main__':
    symbiot_core: SymbiotStarter = SymbiotStarter(dict(
        main=MainEndpoint,
        chat=ChatEndpoint
    )).flask(app).divisions(
        CoreDivision()
    ).listen_all().run(debug=True, port=5001)
