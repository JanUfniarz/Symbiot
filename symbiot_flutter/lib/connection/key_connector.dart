import "package:symbiot_flutter/connection/http_facade.dart";

import "../models/endpoint_model.dart";

class KeyConnector extends HTTPFacade {
  final EndpointModel keyEndpoint = EndpointModel(Receiver.server, "key");

  void provideKeys(Map<String, String> keys) => post(keyEndpoint, body: keys);

  void clearKey(String name) => delete(keyEndpoint, pathArgument: name);
}