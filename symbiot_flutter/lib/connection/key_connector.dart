// ignore_for_file: curly_braces_in_flow_control_structures, avoid_print

import "dart:convert";

import "package:http/http.dart" as http;
import "package:symbiot_flutter/connection/connection_provider.dart";

class KeyConnector {
  final String path = "key";

  void provideKeys(Map<String, String> keys) =>
      ConnectionProvider.post(path, body: keys);
}