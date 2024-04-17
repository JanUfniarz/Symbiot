import 'package:flutter/material.dart';

import '../style/palette.dart';

// ignore: must_be_immutable
class InputBar extends StatelessWidget {
  final void Function(String) onSend;
  final TextEditingController? textController;

  InputBar({super.key,
    required this.onSend,
    String? text,
  }): textController = text == null ? null
      : TextEditingController(text: text);

  String? value;

  @override
  Widget build(BuildContext context) => Row(
    children: <Widget>[

      Flexible(
        child: TextField(
          controller: textController,
          decoration: const InputDecoration(
            filled: true,
            fillColor: Palette.accent,
            hintText: 'Wpisz wiadomość...',
          ),
          onChanged: (text) => value = text,
          onSubmitted: (text) => onSend(text),
          maxLines: null,
        ),
      ),

      IconButton(
        iconSize: 30,
        color: Palette.primary,
        icon: const Icon(Icons.send),
        onPressed: () => value != null
            ? onSend(value!) : null,
      ),
    ],
  );
}
