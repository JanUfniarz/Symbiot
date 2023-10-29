import 'package:symbiot_flutter/connection/http_facade.dart';

import '../models/record_model.dart';

class ChatConnector {

  final String path = "chat";

  Future<dynamic> manageChat(
      String action, {RecordModel? step}
      ) async => (action == "open" || action == "close")
      ? await HTTPFacade.post(path, body: step != null ? {
        "command": action,
        "id": step.id,
        "status": step.status
      } : {"command": action}) : throw ArgumentError(
      "action must be 'open' or 'close'");

  Future<dynamic> sendMessage(String message) async =>
      await HTTPFacade.put(path, body: {"prompt": message});
}