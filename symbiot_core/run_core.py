from flask import Flask
from injector import Injector

from symbiot_core.config.core_division import CoreDivision
from symbiot_core.endpoints.main_endpoint import MainEndpoint

app: Flask = Flask(__name__)

if __name__ == '__main__':
    injector = Injector(CoreDivision(app))
    injector.get(MainEndpoint).listen("main")
    app.run(debug=True, port=5001)
