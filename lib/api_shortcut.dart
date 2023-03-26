import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:iron_man_ai_try_5/palette.dart';

class ApiShortcut extends StatelessWidget {

  static const channel = MethodChannel(
      "com.flutter.main/Channel"
  );
  
  String? apiKey;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Palette.main,
      appBar: AppBar(
        backgroundColor: Palette.accent,
        centerTitle: true,
        title: Text("Symbiot",
          style: TextStyle(
              color: Palette.main,
          ),
        ),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: <Widget>[
          SizedBox(height: 100),
          TextField(
            decoration: InputDecoration(
              hintText: 'Api Key',
              filled: true,
              fillColor: Palette.background,
            ),
            onChanged: (text) => apiKey = text,
          ),
          SizedBox(
            width: 90,
            height: 50,
            child: ElevatedButton(
              onPressed: () async {
                
                Map<String, dynamic> arguments = {
                  "API_KEY" : apiKey
                };
                
                await channel.invokeMethod("setApiKey", arguments);

                Navigator.pushReplacementNamed(context, "/home");
              
              },
              child: Icon(
                Icons.done,
                color: Palette.main,
              ),
              style: ElevatedButton.styleFrom(
                backgroundColor: Palette.accent,
              ),
            ),
          ),
          SizedBox(height: 100),
        ],
      ),
    );
  }
}
