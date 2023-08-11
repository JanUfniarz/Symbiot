from flask import Flask, request, jsonify

app = Flask(__name__)

class AsciiView:
    def __init__(self, method):
        self.method = method

    @staticmethod
    def get_output(inputchr):
        return {'output': str(ord(inputchr))}

    def process_request(self):
        inputchr = str(request.args.get('query', ''))
        return self.get_output(inputchr)

@app.route('/api', methods=['GET', 'PUT', 'DELETE', 'POST'])
def handle_ascii():
    method = request.method
    view = AsciiView(method)
    return jsonify(view.process_request())

if __name__ == '__main__':
    app.run()
