// ignore_for_file: curly_braces_in_flow_control_structures, avoid_print

import "package:symbiot_flutter/connection/http_facade.dart";

class KeyConnector {
  final String path = "key";

  void provideKeys(Map<String, String> keys) =>
      HTTPFacade.post(path, body: keys);

  void clearKey(String name) =>
      HTTPFacade.delete(path, pathArgument: name);
}