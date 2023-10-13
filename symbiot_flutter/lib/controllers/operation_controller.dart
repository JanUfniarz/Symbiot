import 'package:flutter/material.dart';

import '../connection/chat_connector.dart';
import '../connection/operation_connector.dart';
import '../models/operation_model.dart';
import '../models/record_model.dart';

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
  int? pickedIndex;
  int? openedRecordID;

  OperationModel? get model => models != null && pickedIndex != null
      ? models![pickedIndex!] : null;

  RecordModel? get openedRecord => models != null && openedRecordID != null
      ? model!.records.firstWhere(
          (element) => element.id == openedRecordID) : null;

  void openChat(int stepID) {
    openedRecordID = stepID;
    _chatConnector!.manageChat("open", stepID);
    notifyListeners();
  }

  void chat(String message) =>
      _chatConnector!.sendMessage(message)
          .then((val) => openedRecord!
          .body = val["step_body"])
          .whenComplete(() => notifyListeners());

  Future<void> loadData() async => await
      _operationConnector!.getAllOperations()
          .then((val) => models = val
          .map((el) => OperationModel(el))
          .toList(), onError: (er) => print(
          "error loading operation data $er"))
          .whenComplete(() => notifyListeners());

  void newOperation(String wish) => 
      _operationConnector!.createOperation(wish)
          .whenComplete(() => loadData());
}