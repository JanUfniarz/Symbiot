// ignore_for_file: curly_braces_in_flow_control_structure, curly_braces_in_flow_control_structures, avoid_print

import "dart:convert";

import "package:http/http.dart" as http;

class FirstConnector {
  final String url = "http://127.0.0.1:5000/operation";

  FirstConnector();

  Future<dynamic> readData() async {

    final response = await http.get(Uri.parse(url));

    print(response.body);

    if (response.statusCode != 200)
      throw Exception('Failed to load data from server');

    return jsonDecode(utf8.decode(response.bodyBytes));
  }

  Future<dynamic> createData(
      String? argument
      ) async {

    if (argument == null) {
      print("No argument");
      return;
    }

    final response = await http.post(
        Uri.parse("$url/$argument"),
        // body: {

        // }
        );

    if (response.statusCode != 200)
      throw Exception('Failed to post data to server');

    return jsonDecode(utf8.decode(response.bodyBytes));
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

  Future<void> deleteData() async {
    final response = await http.delete(
      Uri.parse(url),
    );

    if (response.statusCode != 200)
      throw Exception('Failed to delete data');
  }
}