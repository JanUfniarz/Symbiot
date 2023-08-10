import 'dart:async';

import 'package:flutter/material.dart';
import 'package:symbiot_flutter/first_connector.dart';

class HomeView extends StatefulWidget {
  final FirstConnector connector;

  const HomeView({super.key, required this.connector});

  @override
  State<HomeView> createState() => _HomeViewState();
}

class _HomeViewState extends State<HomeView> {

  String? name;

  // Future<dynamic> fetchData() async =>
  //     await widget.connector.readData();


  @override
  void initState() {
    widget.connector.readData().then((value) {
      print("val: $value");
      print("mes: ${value["message"]}");
      setState(() => name = value["message"]);
    });
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: name == null
            ? const CircularProgressIndicator()
            : Text(name!),
      ),
    );
  }
}
