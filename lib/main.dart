import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:iron_man_ai_try_5/api_shortcut.dart';
import 'package:iron_man_ai_try_5/palette.dart';

import 'message.dart';

void main() {
  runApp(MaterialApp(
    //? initialRoute: Platform.isAndroid ? "/home" : "/windows",
    initialRoute: "/home",
    routes: {
      "/home" : (context) => const Home(),
      "/api" : (context) => ApiShortcut(),
      //? "/windows" : (context) => WindowsHome(),
    },
  ));
}

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {

  static const channel = MethodChannel(
      "com.flutter.main/Channel"
  );

  String prompt = "";
  List<Widget> messages = [];

void send() async {

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
}

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Palette.main,
        centerTitle: true,
        title: Text("Symbiot",
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
              borderRadius: const BorderRadius.only(
                topLeft: Radius.circular(10),
                topRight: Radius.circular(10),
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
                            padding: const EdgeInsets.symmetric(horizontal: 20),
                            child: RawKeyboardListener(
                              focusNode: FocusNode(),
                              onKey: (RawKeyEvent event) {
                                if (event.logicalKey == LogicalKeyboardKey.enter) {
                                  send();
                                }
                              },
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
                        ),
                        Flexible(
                          flex: 1,
                          child: SizedBox(
                            width: 90,
                            height: 50,
                            child: ElevatedButton(
                             onPressed: () => send(),
                              style: ElevatedButton.styleFrom(
                                backgroundColor: Palette.accent,
                             ),
                              child: Icon(
                               Icons.send,
                               color: Palette.main,
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
