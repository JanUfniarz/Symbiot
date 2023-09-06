// ignore_for_file: curly_braces_in_flow_control_structures, avoid_print

import "dart:convert";

import "package:http/http.dart" as http;

import "connection_provider.dart";

class OperationConnector {

  final String path = "operation";

  Future<dynamic> getAllOperations() async =>
      await ConnectionProvider.get(path);

  Future<dynamic> createOperation(
      String? argument
      ) async {

    if (argument == null) {
      print("No argument");
      return;
    }

    final response = await http.post(
        Uri.parse("$url/$argument"),
        body: {

        }
        );

    if (response.statusCode != 200)
      throw Exception('Failed to post data to server');

    return jsonDecode(utf8.decode(response.bodyBytes));
  }

  Future<void> updateOperation(
      // argumenty
      ) async {

    final response = await http.put(
        Uri.parse(//"$url/$id"
          url
        ),
        //body: {

        //}
    );

    if (response.statusCode != 200)
      throw Exception('Failed to update data');
  }

  Future<void> deleteOperation() async {
    final response = await http.delete(
      Uri.parse(url),
    );

    if (response.statusCode != 200)
      throw Exception('Failed to delete data');
  }
}