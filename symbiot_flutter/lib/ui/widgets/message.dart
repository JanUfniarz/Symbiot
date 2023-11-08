import 'package:flutter/material.dart';
import 'package:symbiot_flutter/models/message_model.dart';

import '../palette.dart';

class Message extends StatelessWidget {
  final MessageModel model;
  final double _messageCornerRadius = 20;

  const Message(this.model, {super.key});

  @override
  Widget build(BuildContext context) => Card(
    elevation: 0,
    color: Palette.background,
    child: Padding(
      padding: const EdgeInsets.symmetric(vertical: 10),
      child: Row(
        mainAxisAlignment: model.axisAlignment,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[

          Flexible(
            child: ClipRRect(
              borderRadius: BorderRadius.only(
                topLeft: Radius.circular(_messageCornerRadius),
                topRight: Radius.circular(_messageCornerRadius),
                bottomLeft: Radius.circular(
                    model.role == Role.assistant ? 0 : _messageCornerRadius
                ),
                bottomRight: Radius.circular(
                    model.role == Role.user ? 0 : _messageCornerRadius
                ),
              ),

              child: Container(
                padding: const EdgeInsets.all(20),
                color: model.color,
                child: Text(model.content,
                  textAlign: model.textAlignment,
                  style: const TextStyle(
                      color: Palette.background,
                      fontSize: 20,
                      backgroundColor: Colors.transparent,
                      height: 1
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    ),
  );
}