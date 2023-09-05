import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../BLoCs/key_manager_bloc.dart';
import '../palette.dart';

class KeysView extends StatelessWidget {
  const KeysView({super.key});

  final List<String> keyNames = const [
    "openAI", "other"
  ];

  @override
  Widget build(BuildContext context) => Consumer<KeyManager>(
    builder: (context, bloc, child) => Scaffold(
      backgroundColor: Palette.background,
      body: ListView(
        children: List.generate(
            keyNames.length,
                (index) => bloc.keys[keyNames[index]] == null
                  ? ElevatedButton(
                    onPressed: () {},
                    child: Text("Add ${keyNames[index]}")
                ) : Text("${keyNames[index]} provided")
        )
      ),
    )
  );
}
