import 'package:flutter/material.dart';

import '../connection/operation_connector.dart';
import '../models/operation_model.dart';

class OperationBloc extends ChangeNotifier {

  OperationBloc._private();
  static final OperationBloc _instance = OperationBloc._private();
  static OperationBloc get instance => _instance;

  OperationConnector? _connector;
  set connector(OperationConnector value) => _connector = value;

  OperationModel? _model;

  Future<void> loadData() async => _connector!.readData()
        .then((value) => _model = OperationModel(value));
}