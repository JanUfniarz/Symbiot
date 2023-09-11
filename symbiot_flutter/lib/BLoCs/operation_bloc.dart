import 'package:flutter/material.dart';

import '../connection/operation_connector.dart';
import '../models/operation_model.dart';

class OperationBloc extends ChangeNotifier {

  OperationConnector? _connector;

  OperationBloc._private();
  static final OperationBloc _instance = OperationBloc._private();

  static OperationBloc getInstance({
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