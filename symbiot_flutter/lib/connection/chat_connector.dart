// ignore_for_file: curly_braces_in_flow_control_structures

import 'package:symbiot_flutter/connection/http_facade.dart';

import '../models/record_model.dart';

class ChatConnector {

  final String path = "chat";

  Future<dynamic> manageChat(
      String action, RecordModel step,
      ) async => (action != "open" && action != "close")
      ? HTTPFacade.post(path, body: {
        "command": action, "id": step.id
      }) : throw ArgumentError(
      "action must be 'open' or 'close'");

  Future<dynamic> sendMessage(String message) async =>
      HTTPFacade.put(path, body: {"prompt": message});
}