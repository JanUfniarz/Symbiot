import 'package:flutter/material.dart';
import 'package:iron_man_ai_try_5/palette.dart';

class Message extends StatefulWidget {

  bool isResponse;
  String text;

  Message({required this.isResponse, required this.text});

  @override
  State<Message> createState() => _MessageState();
}

class _MessageState extends State<Message> {

  @override
  Widget build(BuildContext context) {
    if (widget.isResponse) {
      return Card(
        color: Palette.resCard,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: <Widget>[
            Flexible(
              child: Text("${widget.text}",
                style: TextStyle(
                  color: Palette.accent,
                  fontSize: 20,
                  backgroundColor: Palette.resCard,
                ),
              ),
            ),
            SizedBox(width: 100),
          ],
        ),
      );
    } else {
      return Card(
        color: Palette.background,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: <Widget>[
            SizedBox(width: 100),
            Flexible(
              child: Text("${widget.text}",
                textAlign: TextAlign.end,
                style: TextStyle(
                  color: Palette.main,
                  fontSize: 20,
                  backgroundColor: Palette.background,
                ),
              ),
            ),
          ],
        ),
      );
    }
  }
}
