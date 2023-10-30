// ignore_for_file: curly_braces_in_flow_control_structures, avoid_print

import "../models/endpoint_model.dart";
import "http_facade.dart";

class OperationConnector extends HTTPFacade {

  final EndpointModel mainEndpoint = EndpointModel(Receiver.core, "main");
  final EndpointModel operationEndpoint = EndpointModel(Receiver.server, "operation");

  Future<List<dynamic>> getAllOperations() async => await get(operationEndpoint);

  Future<dynamic> createOperation(String wish) async =>
      await post(mainEndpoint, body: {"wish": wish});
}