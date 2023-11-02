import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../control/controllers/key_controller.dart';
import '../palette.dart';
import '../widgets/bordered_button.dart';
import '../widgets/symbiot_text_field.dart';

class KeysView extends StatelessWidget {
  const KeysView({super.key});

  final List<String> keyNames = const [
    "openAI", "other"
  ];

  @override
  Widget build(BuildContext context) => Consumer<KeyController>(
    builder: (context, controller, child) => Padding(
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
                          controller.keys[keyNames[index]] != null
                              ? const Icon(
                            Icons.done_outline_sharp,
                            color: Palette.primary,
                          )   : const Icon(
                            Icons.cancel_outlined,
                            color: Palette.delete,
                          ),
                         const SizedBox(width: 100),
                         Row(
                            children: controller.keys[keyNames[index]] != null
                                ? <BorderedButton>[
                              BorderedButton(
                                onTap: () => controller.clear(keyNames[index]),
                                icon: Icons.delete,
                                text: "Delete",
                                primaryColor: Palette.delete,
                              ),
                              BorderedButton(
                                  onTap: () => controller.showKey(
                                      context, keyNames[index]
                                  ),
                                  text: "Show",
                                  icon: Icons.remove_red_eye_outlined
                              )
                            ]
                                : <Widget> [
                              controller.indexToAdd == index
                                  ? SymbiotTextField(
                                onChanged: (text) => controller.newKey = text,
                                onSubmitted: (text) {
                                  controller.newKey = text;
                                  controller.setKey(keyNames[index]);
                                },
                              )
                                  : const SizedBox(),
                              BorderedButton(
                                  onTap: () => controller.indexToAdd == index
                                      ? controller.setKey(keyNames[index])
                                      : controller.showTextfield(index),
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