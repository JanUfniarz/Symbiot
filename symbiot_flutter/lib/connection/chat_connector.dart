import 'package:symbiot_flutter/connection/http_facade.dart';
import 'package:symbiot_flutter/models/endpoint_model.dart';

import '../models/record_model.dart';

class ChatConnector extends HTTPFacade {
  final EndpointModel chatEndpoint = EndpointModel(Receiver.core, "chat");

  Future<dynamic> manageChat(
      String action, {RecordModel? step}
      ) async => (action == "open" || action == "close")
      ? await post(chatEndpoint, body: step != null ? {
        "command": action,
        "id": step.id,
        "status": step.status
      } : {"command": action}) : throw ArgumentError(
      "action must be 'open' or 'close'");

  Future<dynamic> sendMessage(String message) async =>
      await put(chatEndpoint, body: {"prompt": message});
}