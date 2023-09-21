import 'package:flutter/material.dart';

import '../connection/operation_connector.dart';
import '../models/operation_model.dart';

class OperationManager extends ChangeNotifier {

  OperationConnector? _connector;

  OperationManager._private();
  static final OperationManager _instance = OperationManager._private();

  static OperationManager getInstance({
    OperationConnector? connector
  }) {
    _instance._connector ??= connector;
    return _instance;
  }

  OperationModel? _model;

  Future<void> loadData() async =>
      _connector!.getAllOperations()
          .then((value) => _model = OperationModel(value));
}