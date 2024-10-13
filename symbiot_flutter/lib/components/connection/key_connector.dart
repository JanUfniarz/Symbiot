import '../../models/endpoint_model.dart';
import 'http_facade.dart';

class KeyConnector extends HTTPFacade {
  final EndpointModel keyEndpoint = EndpointModel(Receiver.engine, "key");

  void provideKeys(Map<String, String> keys) => post(keyEndpoint, body: keys);

  void clearKey(String name) => delete(keyEndpoint, pathArgument: name);
}