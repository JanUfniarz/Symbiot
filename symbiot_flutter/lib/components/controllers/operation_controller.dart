import 'package:flutter/cupertino.dart';

import '../../models/operation_model.dart';
import '../../models/record_model.dart';
import '../connection/operation_connector.dart';
import '../internal_cache.dart';

class OperationController extends ChangeNotifier {
  final OperationConnector operationConnector;
  final InternalCache cache;

  bool _multiPurposeTrigger;

  OperationController(this.operationConnector, this.cache):
        _multiPurposeTrigger = false;

  Future<void> loadData() async => await
    operationConnector.getAllOperations()
        .then((val) => cache.operations = val)
        .whenComplete(() => notifyListeners());

  dynamic trigger({bool get = false}) {
    if (get) return _multiPurposeTrigger;
    _multiPurposeTrigger = !_multiPurposeTrigger;
    notifyListeners();
  }

  OperationModel operation(String id) => cache.operations
      .firstWhere((el) => el.id == id);

  RecordModel record(String id) => cache.records
      .firstWhere((el) => el.id == id);
}