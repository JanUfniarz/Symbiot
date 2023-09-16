// ignore_for_file: curly_braces_in_flow_control_structures, avoid_print

import "http_facade.dart";

class OperationConnector {

  final String path = "operation";

  Future<dynamic> getAllOperations() async =>
      await HTTPFacade.get(path);

  Future<dynamic> createOperation(
      String? argument) async {

    if (argument == null)
      throw Exception("No argument");

    return HTTPFacade.post(path,
        pathArgument: argument,
    );
  }

  Future<void> updateOperation() async {}

  Future<void> deleteOperation() async => HTTPFacade.delete(path);
}