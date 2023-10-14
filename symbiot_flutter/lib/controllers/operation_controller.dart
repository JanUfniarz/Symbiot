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

  List<OperationModel>? models;
  int? _pickedModelID;

  OperationModel? get model => models != null && _pickedModelID != null
      ? models!.firstWhere((el) => el.id == _pickedModelID) : null;

  RecordModel record(int id) => model!.records.firstWhere((el) => el.id == id);

  void openOperation(int id, BuildContext context) {
    _pickedModelID = id;
    SymbiotApp.push(
        context, const OperationView()
    ).whenComplete(() => loadData());
  }

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