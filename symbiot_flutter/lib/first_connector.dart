// ignore_for_file: curly_braces_in_flow_control_structure, curly_braces_in_flow_control_structures

import "dart:convert";

import "package:http/http.dart" as http;

class FirstConnector {
  final String url = "http://127.0.0.1:5000";

  FirstConnector();

  Future<dynamic> readData() async {
    final response = await http.get(Uri.parse(url),
    );

    if (response.statusCode != 200)
      throw Exception('Failed to load data from server');

    return jsonDecode(utf8.decode(response.bodyBytes));
  }

  Future<void> createData(
      // argumenty
      ) async {
    final response = await http.post(
        Uri.parse(url),
        // body: {

        // }
        );

    if (response.statusCode != 201)
      throw Exception('Failed to post data to server');
  }

  Future<void> updateData(
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

  Future<void> deleteData(int id) async {
    final response = await http.delete(
      Uri.parse('$url/$id'),
    );

    if (response.statusCode != 200)
      throw Exception('Failed to delete data');
  }
}