class EndpointModel {
  int _port;
  String path;
  Map<String, String> headers;

  EndpointModel(
      Receiver receiver,
      this.path,
      {Map<String, String>? headers}):
        _port = _receiverToPort(receiver),
        headers = headers ?? {
        "Content-Type": "application/json; charset=UTF-8",
      };

  static int _receiverToPort(Receiver receiver) {
    switch (receiver) {
      case Receiver.server: return 5000;
      case Receiver.engine: return 5001;
    }
  }

  set receiver(Receiver value) => _port = _receiverToPort(value);

  Receiver get receiver => _port == 5000 ? Receiver.server : Receiver.engine;

  Uri uri(String? arg) => Uri.parse(
      "http://127.0.0.1:$_port/$path/${arg ?? ""}"
  );
}

enum Receiver {
  server, engine
}