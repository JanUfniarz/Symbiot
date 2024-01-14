import 'package:symbiot_flutter/models/endpoint_model.dart';

import '../../models/record_model.dart';
import 'http_facade.dart';

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
      await put(chatEndpoint,
          pathArgument: "prompt",
          body: {"prompt": message});

  Future<dynamic> setBody(String newBody) async =>
      await put(chatEndpoint,
          pathArgument: "body",
          body: {"new_body": newBody});
}