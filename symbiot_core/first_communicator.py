import json
import socket
import threading


class FirstCommunicator:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)

    def _handle_client(self, client_socket):
        request_json = client_socket.recv(1024).decode()
        request_data = json.loads(request_json)

        # Przetwarzanie zapytania
        response_data = {"response": "Odpowiedź na zapytanie"}

        response_json = json.dumps(response_data)
        client_socket.send(response_json.encode())

        client_socket.close()

    def receive(self):
        while True:
            client, addr = self.server.accept()
            client_handler = threading.Thread(target=self._handle_client, args=(client,))
            client_handler.start()


# Użycie
communication = FirstCommunicator("localhost", 4040)
communication.receive()
