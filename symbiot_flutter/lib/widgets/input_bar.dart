import 'package:flutter/material.dart';

import '../palette.dart';

class InputBar extends StatelessWidget {
  const InputBar({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.bottomCenter,
      padding: const EdgeInsets.symmetric(
          horizontal: 70,
          vertical: 20
      ),
      child: Row(
        children: <Widget>[

          Flexible(
            child: TextField(
              decoration: const InputDecoration(
                filled: true,
                fillColor: Palette.accent,
                hintText: 'Wpisz wiadomość...',
              ),
              onChanged: (text) {},
              onSubmitted: (text) {},
              maxLines: null,
            ),
          ),

          IconButton(
            iconSize: 30,
            color: Palette.primary,
            icon: const Icon(Icons.send),
            onPressed: () {},
          ),
        ],
      ),
    );
  }
}
