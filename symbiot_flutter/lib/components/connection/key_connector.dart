import '../../models/endpoint_model.dart';
import 'http_facade.dart';

class KeyConnector extends HTTPFacade {
  final EndpointModel _keyEndpoint = EndpointModel(Receiver.engine, "key");

  void provideKeys(Map<String, String> keys) => post(_keyEndpoint, body: keys);

  void clearKey(String name) => delete(_keyEndpoint, pathArgument: name);
}