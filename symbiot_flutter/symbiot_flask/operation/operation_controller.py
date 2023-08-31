import json

from flask import jsonify


class OperationController:

    def __init__(self, app, path, service):
        self.app = app
        self.path = path
        self.service = service

        @app.route(path + "/", methods=["GET"])
        def get_operation():
            operations_dicts = [op.__dict__ for op in service.operation_data()]
            for op in operations_dicts:
                op.pop("_sa_instance_state")
            return jsonify(operations_dicts)

        @app.route(path + "/", methods=["PUT"])
        def update_operation():
            pass

        @app.route(path + '/<string:arg>', methods=["POST"])
        def add_operation(arg):

            service.create(arg)
            # command, execute = service.create(arg)
            #
            # return jsonify(
            #     {"command": command,
            #      "execute": execute})
            return jsonify({"arg": arg})

        @app.route(path + "/", methods=["DELETE"])
        def guide_delete():
            pass
