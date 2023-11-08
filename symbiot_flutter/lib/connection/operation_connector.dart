import "../models/endpoint_model.dart";
import "http_facade.dart";

class OperationConnector extends HTTPFacade {

  final EndpointModel mainEndpoint = EndpointModel(Receiver.core, "main");
  final EndpointModel operationEndpoint = EndpointModel(Receiver.server, "operation");

  Future<List<dynamic>> getAllOperations() async => await get(operationEndpoint);

  Future<dynamic> createOperation(String wish) async =>
      await post(mainEndpoint, body: {"wish": wish});

  Future<dynamic> deleteOperation(String id) async =>
      await delete(operationEndpoint, body: {"id": id});

  Future<dynamic> changeName(String id, String newName) async =>
      await put(operationEndpoint, body: {
        "id": id,
        "to_change": "name",
        "value": newName });
}