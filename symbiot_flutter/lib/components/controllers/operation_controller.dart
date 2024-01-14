import 'package:flutter/material.dart';

import '../../models/operation_model.dart';
import '../../models/record_model.dart';
import '../../ui/symbiot_app.dart';
import '../../ui/views/chat_view.dart';
import '../../ui/views/operation_view.dart';
import '../../ui/widgets/message_change_field.dart';
import '../connection/chat_connector.dart';
import '../connection/operation_connector.dart';

typedef _BodyManipulator = void Function(List<String> entries);

class OperationController extends ChangeNotifier {

  OperationConnector? _operationConnector;
  ChatConnector? _chatConnector;
  List<OperationModel> models = [];

  bool _multiPurposeTrigger = false;

  OperationController._private();

  static final OperationController _instance = OperationController._private();

  static OperationController getInstance({
    OperationConnector? operationConnector,
    ChatConnector? chatConnector
  }) {
    _instance._operationConnector ??= operationConnector;
    _instance._chatConnector ??= chatConnector;
    _instance.loadData();
    return _instance;
  }

  Future<void> loadData() async => await
      _operationConnector!.getAllOperations()
          .then((val) => models = val
          .map((el) => OperationModel(el))
          .toList())
          .whenComplete(() => notifyListeners());

  OperationModel operation(String id) => models.firstWhere((el) => el.id == id);

  RecordModel record(String id) => models.expand((el) => el.records)
      .firstWhere((el) => el.id == id);

  dynamic trigger({bool get = false}) {
    if (get) return _multiPurposeTrigger;
    _multiPurposeTrigger = !_multiPurposeTrigger;
    notifyListeners();
  }

  void openOperation(String id, BuildContext context) => SymbiotApp.push(
        context, OperationView(id)
    ).whenComplete(() => loadData());

  void openChat(RecordModel step, BuildContext context) =>
      _chatConnector!.manageChat("open", step: step)
          .whenComplete(() => SymbiotApp.push(context, ChatView(step.id))
          .whenComplete(() => _chatConnector!.manageChat("close")));

  void chat(String message, String id) {
    trigger();
    _chatConnector!.sendMessage(message)
        .then((val) => record(id).body = val["step_body"])
        .whenComplete(() => trigger());
  }

  Future<OperationModel> newOperation(String wish) async {
    List<String> oldModels = models.map((el) => el.id).toList();
    await _operationConnector!.createOperation(wish)
        .whenComplete(() => loadData());
    return operation(models.map((el) => el.id)
        .firstWhere((id) => !oldModels.contains(id)));
  }

  Future<void> deleteOperation(String id, BuildContext context) async =>
      _operationConnector!.deleteOperation(id)
          .then((ig) => SymbiotApp.back(context))
          .whenComplete(() => loadData());

  Future<void> changeOperationName(String id, String newName) async {
    trigger();
    _operationConnector!.changeName(id, newName)
        .whenComplete(() => loadData());
  }

  void _setBodyWrapper(String id, _BodyManipulator manipulator) {
    List<String> entries = record(id).body!.split("<@entry>");
    manipulator(entries);
    _chatConnector!.setBody(entries.join("<@entry>"))
        .whenComplete(() => loadData());
  }

  void deleteMessage(String id, int index) =>
      _setBodyWrapper(id, (entries) => entries.removeAt(index + 1));
  
  void changeMessage(String id, int index, BuildContext context) =>
      SymbiotApp.bottomSheet(context, MessageChangeField(
          oldMessage: record(id).body!.split("<@entry>")[index + 1]
      )).then((newMessage) => newMessage != null
          ? _setBodyWrapper(id, (entries) => entries[index + 1] = newMessage)
          : null);
}