from flask import Flask, jsonify
from flask.views import MethodView

app = Flask(__name__)

class HelloWorldView(MethodView):
    def get(self):
        response = {
            'message': 'Hello, World!'
        }
        return jsonify(response)

hello_world_view = HelloWorldView.as_view('hello_world_view')
app.add_url_rule('/hello', view_func=hello_world_view, methods=['GET'])

if __name__ == '__main__':
    app.run()
