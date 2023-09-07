from flask import Flask, request, jsonify
from injector import inject

from creative_division.creative_service import CreativeService


class KeysController:
    @inject
    def __init__(self, app: Flask, service: CreativeService):
        self.app = app
        self.service = service

    def listen(self, path):
        @self.app.route(path + "/", methods=['POST'])
        def provide_keys():
            keys = request.get_json()
            self.service.distribute_keys(
                open_ai=keys["openAI"])
            return jsonify({"message": "done!"})

        @self.app.route(path + "/<string:name>", methods=['DELETE'])
        def clear_key(name):
            print("remove " + name)
            # TODO: implement
            return jsonify({"message": "done!"})
