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

  List<OperationModel>? models;
  int? pickedIndex;

  OperationModel model() => models!
      .firstWhere((el) => el.id == pickedIndex);

  Future<void> loadData() async => await
      _connector!.getAllOperations()
          .then((value) => models = value
          .map((el) => OperationModel(el))
          .toList())
          .then((ig) => notifyListeners());
}