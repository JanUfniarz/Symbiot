import "dart:convert";
import "package:http/http.dart" as http;

import "../../models/endpoint_model.dart";


class HTTPFacade {
  Future<dynamic> get(EndpointModel endpoint,
      {String? pathArgument}) async =>
      _manage(await http.get(endpoint.uri(pathArgument)));

  Future<dynamic> post(EndpointModel endpoint,
      {String? pathArgument, Object? body}) async =>
      _manage(await http.post(endpoint.uri(pathArgument),
          headers: endpoint.headers, body: jsonEncode(body ?? {})));

  Future<void> put(EndpointModel endpoint,
      {String? pathArgument, Object? body}) async =>
      _manage(await http.put(endpoint.uri(pathArgument),
          headers: endpoint.headers, body: jsonEncode(body ?? {})));

  Future<void> delete(EndpointModel endpoint,
      {String? pathArgument, Object? body}) async =>
      _manage(await http.delete(endpoint.uri(pathArgument),
          headers: endpoint.headers, body: jsonEncode(body ?? {})));

  dynamic _manage(http.Response response) =>
      response.statusCode == 200
          ? jsonDecode(utf8.decode(response.bodyBytes))
          : throw Exception('Connection error!!!\n'
          'status code: ${response.statusCode}');
}