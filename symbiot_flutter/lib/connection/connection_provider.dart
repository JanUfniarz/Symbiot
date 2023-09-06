// ignore_for_file: curly_braces_in_flow_control_structures, avoid_print

import "dart:convert";

import "package:http/http.dart" as http;

class ConnectionProvider {
  static const String url = "http://127.0.0.1:5000";

  static Future<dynamic> get(path,
      {String? pathArgument}) async =>
      _manage(await http.get(Uri.parse(
          "$url/$path/${pathArgument ?? ""}")));

  static Future<dynamic> post(path,
      {String? pathArgument, Object? body}) async =>
      _manage(await http.post(Uri.parse(
          "$url/$path/${pathArgument ?? ""}"
      ), body: jsonEncode(body)));

  static Future<void> put(path,
      {String? pathArgument, Object? body}) async =>
      _manage(await http.put(Uri.parse(
          "$url/$path/${pathArgument ?? ""}"
      ), body: jsonEncode(body)));

  static Future<void> delete(path,
      {String? pathArgument, Object? body}) async =>
      _manage(await http.put(Uri.parse(
          "$url/$path/${pathArgument ?? ""}"
      ), body: jsonEncode(body)));

  static dynamic _manage(http.Response response) =>
      response.statusCode == 200
          ? jsonDecode(utf8.decode(response.bodyBytes))
          : throw Exception('Serwer connection error!!!');
}