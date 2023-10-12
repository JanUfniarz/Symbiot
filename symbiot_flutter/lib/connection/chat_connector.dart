// ignore_for_file: curly_braces_in_flow_control_structures

import 'package:symbiot_flutter/connection/http_facade.dart';

class ChatConnector {

  final String path = "chat";

  Future<dynamic> manageChat(
      String action, int stepID,
      ) async => (action == "open" || action == "close")
      ? HTTPFacade.post(path, body: {
        "command": action, "id": stepID
      }) : throw ArgumentError(
      "action must be 'open' or 'close'");

  Future<dynamic> sendMessage(String message) async =>
      HTTPFacade.put(path, body: {"prompt": message});
}