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

  OperationModel? _model;

  Future<void> loadData() async =>
      _connector!.getAllOperations()
          .then((value) => _model = OperationModel(value));
}