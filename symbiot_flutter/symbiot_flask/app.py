from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def get():
    response = {
        'message': 'hello'
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
