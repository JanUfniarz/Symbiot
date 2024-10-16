import 'package:symbiot_flutter/models/operation_model.dart';
import 'package:symbiot_flutter/models/record_model.dart';

class InternalCache {
  Map<String, String> keys = {};
  List<OperationModel> _operations = [];

  final _IDStorage _newIds = _IDStorage();

  set operations(List<dynamic> value) {
    Iterable<OperationModel> models = value
        .map((el) => OperationModel(el));

    _newIds
      ..operations = models
          .map((operation) => operation.id)
          .where((id) => !_operations
            .map((operation) => operation.id)
            .contains(id))
          .toList()
      ..records = models
          .expand((el) => el.records)
          .map((record) => record.id)
          .where((id) => !_operations
            .expand((el) => el.records)
            .map((operation) => operation.id)
            .contains(id))
          .toList();

    _operations = models.toList();
  }

  List<OperationModel> get operations => _operations;

  List<RecordModel> get records => _operations
      .expand((operation) => operation.records)
      .toList();

  List<OperationModel> get newOperations => _operations
      .where((operation) => _newIds.operations
        .contains(operation.id))
      .toList();

  List<RecordModel> get newRecords => records
      .where((record) => _newIds.records
        .contains(record.id))
      .toList();
}

class _IDStorage {
  List<String> operations = [];
  List<String> records = [];
}