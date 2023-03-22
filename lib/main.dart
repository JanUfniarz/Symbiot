import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:iron_man_ai_try_5/palette.dart';

import 'message.dart';

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

  String prompt = "";
  List<Widget> messages = [];

  Future<String> _response(arguments) async {
    String r = await channel
        .invokeMethod("respond", arguments);
    return r;
}

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Palette.main,
        centerTitle: true,
        title: Text("Venom",
          style: TextStyle(
            color: Palette.accent
          ),
        ),
      ),
      backgroundColor: Palette.background,
      body: Stack(
        //mainAxisAlignment: MainAxisAlignment.end,
        //crossAxisAlignment: CrossAxisAlignment.stretch,
        children: <Widget>[
          SizedBox(
            height: 570,
            child: Align(
              alignment: Alignment.bottomCenter,
              child: SingleChildScrollView(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: messages,
                ),
              ),
            ),
          ),
          Align(
            alignment: Alignment.bottomCenter,
            child: ClipRRect(
              borderRadius: BorderRadius.only(
                topLeft: Radius.circular(30),
                topRight: Radius.circular(30),
              ),
              child: SizedBox(
                height: 200,
                child: Container(
                  color: Palette.main,
                  child: Center(
                    child: Row(
                      children: <Widget>[
                        Flexible(
                          flex: 2,
                          child: Padding(
                            padding: EdgeInsets.symmetric(horizontal: 20),
                            child: TextField(
                              decoration: InputDecoration(
                                hintText: 'Prompt',
                                filled: true,
                                fillColor: Palette.background,
                              ),
                              onChanged: (text) => prompt = text,
                            ),
                          ),
                        ),
                        Flexible(
                          flex: 1,
                          child: SizedBox(
                            width: 90,
                            height: 50,
                            child: ElevatedButton(
                             onPressed: () async {

                               Map<String, dynamic> arguments = {
                                 "prompt" : prompt
                               };

                               String response = await channel
                                   .invokeMethod("respond", arguments);

                               setState(() {
                                 messages.add(Message(
                                     isResponse: false,
                                     text: prompt));

                                 messages.add(Message(
                                     isResponse: true,
                                     text: response));
                               });

                             },
                              child: Icon(
                               Icons.send,
                               color: Palette.main,
                              ),
                              style: ElevatedButton.styleFrom(
                                backgroundColor: Palette.accent,
                             ),
                           ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }


}
