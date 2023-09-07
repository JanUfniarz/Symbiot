// ignore_for_file: curly_braces_in_flow_control_structures, avoid_print

import "connection_provider.dart";

class OperationConnector {

  final String path = "operation";

  Future<dynamic> getAllOperations() async =>
      await ConnectionProvider.get(path);

  Future<dynamic> createOperation(
      String? argument) async {

    if (argument == null)
      throw Exception("No argument");

    return ConnectionProvider.post(path,
        pathArgument: argument,
    );
  }

  Future<void> updateOperation() async {}

  Future<void> deleteOperation() async {}
}