import 'dart:convert';

import 'package:flutter/material.dart';

import '../style/palette.dart';
import '../symbiot_app.dart';
import 'input_bar.dart';

class MessageChangeField extends StatelessWidget {
  final Map<String, dynamic> oldMessage;

  MessageChangeField({super.key, required String oldMessage}):
        oldMessage = jsonDecode(oldMessage);

  String _format(String newMessage) {
    Map<String, dynamic> res = Map.from(oldMessage);
    res["content"] = newMessage;
    return jsonEncode(res);
  }

  @override
  Widget build(BuildContext context) => Column(
    mainAxisAlignment: MainAxisAlignment.center,
    crossAxisAlignment: CrossAxisAlignment.center,
    children: <Widget> [

      const Text(
        "Change a message",
        style: TextStyle(
          color: Palette.primary,
          fontSize: 30,
        ),
      ),

      Padding(
        padding: const EdgeInsets.all(20),
        child: InputBar(
          text: oldMessage["content"],
          icon: Icons.drive_file_rename_outline_sharp,
          onSend: (newMessage) => SymbiotApp.back(context,
              result: _format(newMessage))),
      ),

    ],
  );
}