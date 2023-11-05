import 'package:flutter/material.dart';

import '../../models/message_model.dart';
import '../palette.dart';

class Message extends StatelessWidget {
  final MessageModel model;

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
              borderRadius: const BorderRadius.only(
                topLeft: Radius.circular(16),
                topRight: Radius.circular(16),
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