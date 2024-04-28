import 'package:flutter/material.dart';
import 'package:symbiot_flutter/components/connection/chat_connector.dart';
import 'package:symbiot_flutter/components/internal_cache.dart';

import '../../models/record_model.dart';
import '../../ui/symbiot_app.dart';
import '../../ui/widgets/message_change_field.dart';
import '../connection/operation_connector.dart';
import 'operation_controller.dart';

class ChatController extends OperationController {
  final ChatConnector _chatConnector;
  final String _entryTag = "<@entry>";

  ChatController(
      OperationConnector operationConnector,
      InternalCache cache,
      this._chatConnector
      ): super(operationConnector, cache);

  void chat(String message, String id) async {
    // TODO: reloading
    trigger();
    var val = await _chatConnector.sendMessage(message);

    if (!val["must_reload"]) record(id).body = val["step_body"];


    trigger();
  }

  void openChat(String stepID) =>
      _chatConnector.manageChat("open", step: record(stepID));

  void closeChat() => _chatConnector.manageChat("close");

  void deleteMessage(String id, int index) =>
      _setBodyWrapper(id, (entries) => entries.removeAt(index + 1));

  void changeMessage(String id, int index, BuildContext context) =>
      SymbiotApp.bottomSheet(context, MessageChangeField(
          oldMessage: record(id).body!.split(_entryTag)[index + 1]
      )).then((newMessage) => newMessage == null ? null
          : _setBodyWrapper(id, (entries) => entries[index + 1] = newMessage));

  void _setBodyWrapper(String id, void Function(List<String> entries) manipulator) {
    List<String> entries = record(id).body!.split(_entryTag);
    manipulator(entries);
    _chatConnector.setBody(entries.join(_entryTag))
        .whenComplete(() => loadData());
  }
}