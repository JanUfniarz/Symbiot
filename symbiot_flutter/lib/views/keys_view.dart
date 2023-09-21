import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/widgets/symbiot_text_field.dart';

import '../managers/key_manager.dart';
import '../palette.dart';
import '../widgets/bordered_button.dart';

class KeysView extends StatelessWidget {
  const KeysView({super.key});

  final List<String> keyNames = const [
    "openAI", "other"
  ];

  @override
  Widget build(BuildContext context) => Consumer<KeyManager>(
    builder: (context, manager, child) => Padding(
      padding: const EdgeInsets.symmetric(vertical: 20),
      child: Column(
        children: List.generate(
            keyNames.length,
                (index) =>
                Padding(
                  padding: const EdgeInsets.symmetric(vertical: 10),
                  child: Center(
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: <Widget>[
                          SizedBox(
                            width: 100,
                            child: Text(
                              "${keyNames[index]} ",
                              style: const TextStyle(
                                color: Palette.accent,
                                fontSize: 20,
                              ),
                            ),
                          ),
                         manager.keys[keyNames[index]] != null
                              ? const Icon(
                            Icons.done_outline_sharp,
                            color: Palette.primary,
                          )   : const Icon(
                            Icons.cancel_outlined,
                            color: Palette.delete,
                          ),
                         const SizedBox(width: 100),
                         Row(
                            children: manager.keys[keyNames[index]] != null
                                ? <BorderedButton>[
                              BorderedButton(
                                onTap: () => manager.clear(keyNames[index]),
                                icon: Icons.delete,
                                text: "Delete",
                                primaryColor: Palette.delete,
                              ),
                              BorderedButton(
                                  onTap: () => manager.showKey(
                                      context, keyNames[index]
                                  ),
                                  text: "Show",
                                  icon: Icons.remove_red_eye_outlined
                              )
                            ]
                                : <Widget> [
                              manager.indexToAdd == index
                                  ? SymbiotTextField(
                                onChanged: (text) => manager.newKey = text,
                                onSubmitted: (text) {
                                  manager.newKey = text;
                                  manager.setKey(keyNames[index]);
                                },
                              )
                                  : const SizedBox(),
                              BorderedButton(
                                  onTap: () => manager.indexToAdd == index
                                      ? manager.setKey(keyNames[index])
                                      : manager.showTextfield(index),
                                  text: "Add",
                                  icon: Icons.add
                              )
                            ]
                          )
                        ],
                      )
                  ),
                )
        ),
      ),
    ),
  );
}