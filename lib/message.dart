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

    return Card(
      elevation: 0,
      color: Palette.background,
      child: Row(
        mainAxisAlignment: widget.isResponse
              ? MainAxisAlignment.start
              : MainAxisAlignment.end,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          //SizedBox(width: widget.isResponse ? 0 : 100),
          Flexible(
            child: ClipRRect(
              borderRadius: BorderRadius.only(
                topLeft: Radius.circular(4),
                topRight: Radius.circular(4),
              ),
              child: Container(
                color: widget.isResponse ? Palette.response : Palette.prompt,
                child: Text("${widget.text}",
                  textAlign: widget.isResponse ? TextAlign.start : TextAlign.end,
                  style: TextStyle(
                    color: widget.isResponse ? Palette.fontLight : Palette.accent,
                    fontSize: 20,
                    backgroundColor: Colors.transparent,
                  ),
                ),
              ),
            ),
          ),
          //SizedBox(width: widget.isResponse ? 0: 100),
        ],
      ),
    );
  }
}
