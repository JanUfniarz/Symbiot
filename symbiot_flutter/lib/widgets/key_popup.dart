import 'package:flutter/material.dart';
import 'package:symbiot_flutter/palette.dart';

import 'button.dart';

class KeyPopup extends StatelessWidget {

  final String name;
  final String apiKey;

  const KeyPopup({super.key,
    required this.name,
    required this.apiKey
  });

  final TextStyle _textStyle = const TextStyle(
    color: Palette.accent,
  );

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: Text('Key: $name', style: _textStyle),
      content: Text(apiKey, style: _textStyle),
      backgroundColor: Palette.background,
      actions: <Widget>[
        Button(
          text: "close",
          icon: Icons.close,
          primaryColor: Palette.accent,
          onTap: () {
            Navigator.of(context).pop();
          },
        ),
      ],
    );
  }
}
