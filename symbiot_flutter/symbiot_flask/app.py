from flask import Flask, jsonify
from flask.views import MethodView

app = Flask(__name__)

class ExampleView(MethodView):
    def get(self):
        response = {
            'message': 'This is a GET request example.'
        }
        return jsonify(response)

    def post(self):
        data = request.json
        response = {
            'message': 'This is a POST request example.',
            'received_data': data
        }
        return jsonify(response)

    def put(self):
        data = request.json
        response = {
            'message': 'This is a PUT request example.',
            'received_data': data
        }
        return jsonify(response)

    def delete(self):
        response = {
            'message': 'This is a DELETE request example.'
        }
        return jsonify(response)

example_view = ExampleView.as_view('example_view')
app.add_url_rule('/example', view_func=example_view, methods=['GET', 'POST', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run()
