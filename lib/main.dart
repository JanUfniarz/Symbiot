import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() {
  runApp(MaterialApp(
    initialRoute: "/home",
    routes: {
      "/home" : (context) => Home(),
    },
  ));
}

class Home extends StatefulWidget {

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {

  static const channel = MethodChannel(
      "com.flutter.main/Channel"
  );

  int value = 0;
  int pyRes = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: <Widget>[
          TextField(
            decoration: InputDecoration(
                hintText: 'Balance',
                filled: true,
                fillColor: Colors.grey
            ),
            keyboardType: TextInputType.number,
            onChanged: (text) => value = int.parse(text),
          ),
          Text(pyRes.toString()),
          ElevatedButton(
            onPressed: () async {
              var arguments = <String, dynamic> {
                "value" : value,
              };

              int temp = await channel.invokeMethod(
                  "square",
                  arguments
              );

              setState(() => pyRes = temp);
            },
            child: Text("test"),
          ),
        ],
      ),
    );
  }
}
