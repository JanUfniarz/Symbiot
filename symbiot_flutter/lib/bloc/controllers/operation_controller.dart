import 'package:flutter/material.dart';

import '../../connection/chat_connector.dart';
import '../../connection/operation_connector.dart';
import '../../models/operation_model.dart';
import '../../models/record_model.dart';
import '../../ui/symbiot_app.dart';
import '../../ui/views/chat_view.dart';
import '../../ui/views/operation_view.dart';

class OperationController extends ChangeNotifier {

  OperationConnector? _operationConnector;
  ChatConnector? _chatConnector;
  List<OperationModel> models = [];

  OperationController._private();

  static final OperationController _instance = OperationController._private();

  static OperationController getInstance({
    OperationConnector? operationConnector,
    ChatConnector? chatConnector
  }) {
    _instance._operationConnector ??= operationConnector;
    _instance._chatConnector ??= chatConnector;
    return _instance;
  }

  OperationModel operation(String id) => models.firstWhere((el) => el.id == id);

  RecordModel record(String id) => models.expand((el) => el.records)
      .firstWhere((el) => el.id == id);

  void openOperation(String id, BuildContext context) => SymbiotApp.push(
        context, OperationView(id)
    ).whenComplete(() => loadData());

  void openChat(RecordModel step, BuildContext context) =>
    _chatConnector!.manageChat("open", step: step)
        .whenComplete(() => SymbiotApp.push(context, ChatView(step.id))
        .whenComplete(() => _chatConnector!.manageChat("close")));

  void chat(String message, String id) =>
      _chatConnector!.sendMessage(message)
          .then((val) => record(id).body = val["step_body"])
          .whenComplete(() => notifyListeners());

  Future<void> loadData() async => await
      _operationConnector!.getAllOperations()
          .then((val) => models = val
          .map((el) => OperationModel(el))
          .toList())
          .whenComplete(() => notifyListeners());

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
}