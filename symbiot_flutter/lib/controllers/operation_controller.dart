import 'package:flutter/material.dart';

import '../connection/operation_connector.dart';
import '../models/operation_model.dart';

class OperationController extends ChangeNotifier {

  OperationConnector? _connector;

  OperationController._private();
  static final OperationController _instance = OperationController._private();

  static OperationController getInstance({
    OperationConnector? connector
  }) {
    _instance._connector ??= connector;
    return _instance;
  }

  List<OperationModel>? _models;
  int? pickedID;

  OperationModel model() => _models!
      .firstWhere((el) => el.id == pickedID);

  Future<void> loadData() async =>
      _connector!.getAllOperations()
          .then((value) => _models = value
          .map((el) => OperationModel(el))
          .toList());
}