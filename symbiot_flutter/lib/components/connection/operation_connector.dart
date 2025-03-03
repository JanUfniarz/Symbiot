import "../../models/endpoint_model.dart";
import "http_facade.dart";

class OperationConnector extends HTTPFacade {

  final EndpointModel _mainEndpoint = EndpointModel(Receiver.engine, "main");
  final EndpointModel _operationEndpoint = EndpointModel(Receiver.server, "operation");

  Future<List<dynamic>> getAllOperations() async => await get(_operationEndpoint);

  Future<dynamic> createOperation(String wish) async =>
      await post(_mainEndpoint, body: {"wish": wish});

  Future<dynamic> deleteOperation(String id) async =>
      await delete(_operationEndpoint, body: {"id": id});

  Future<dynamic> changeName(String id, String newName) async =>
      await put(_operationEndpoint, body: {
        "id": id,
        "to_change": "name",
        "value": newName });
}