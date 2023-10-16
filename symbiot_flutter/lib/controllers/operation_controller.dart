import 'package:flutter/material.dart';
import 'package:symbiot_flutter/symbiot_app.dart';

import '../connection/chat_connector.dart';
import '../connection/operation_connector.dart';
import '../models/operation_model.dart';
import '../models/record_model.dart';
import '../views/chat_view.dart';
import '../views/operation_view.dart';

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

  OperationModel operation(int id) => models.firstWhere((el) => el.id == id);

  RecordModel record(int id) => models.expand((el) => el.records)
      .firstWhere((el) => el.id == id);

  void openOperation(int id, BuildContext context) => SymbiotApp.push(
        context, OperationView(id)
    ).whenComplete(() => loadData());

  void openChat(int stepID, BuildContext context) {
    _chatConnector!.manageChat("open", stepID);
    SymbiotApp.push(
        context, ChatView(stepID))
        .whenComplete(
            () => _chatConnector!.manageChat("close", stepID)
                .whenComplete(() => notifyListeners()));
  }

  void chat(String message, int id) =>
      _chatConnector!.sendMessage(message)
          .then((val) => record(id).body = val["step_body"])
          .whenComplete(() => notifyListeners());

  Future<void> loadData() async => await
      _operationConnector!.getAllOperations()
          .then((val) => models = val
          .map((el) => OperationModel(el))
          .toList())
          .whenComplete(() => notifyListeners());

  void newOperation(String wish) => 
      _operationConnector!.createOperation(wish)
          .whenComplete(() => loadData());
}