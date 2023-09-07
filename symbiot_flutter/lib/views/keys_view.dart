import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/widgets/symbiot_text_field.dart';

import '../BLoCs/key_manager_bloc.dart';
import '../palette.dart';
import '../widgets/button.dart';
import '../widgets/symbiot_scaffold.dart';

class KeysView extends StatelessWidget {
  const KeysView({super.key});

  final List<String> keyNames = const [
    "openAI", "other"
  ];

  @override
  Widget build(BuildContext context) => Consumer<KeyManager>(
    builder: (context, bloc, child) => SymbiotScaffold(
      tittle: "Api Keys",
      body: Padding(
        padding: const EdgeInsets.symmetric(vertical: 20),
        child: ListView(
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

                            bloc.keys[keyNames[index]] != null
                                ? const Icon(
                              Icons.done_outline_sharp,
                              color: Palette.primary,
                            )   : const Icon(
                              Icons.cancel_outlined,
                              color: Palette.delete,
                            ),

                            const SizedBox(width: 100),

                            Row(
                              children: bloc.keys[keyNames[index]] != null
                                  ? <Button>[
                                Button(
                                  onTap: () => bloc.clear(keyNames[index]),
                                  icon: Icons.delete,
                                  text: "Delete",
                                  primaryColor: Palette.delete,
                                ),
                                Button(
                                    onTap: () => bloc.showKey(
                                        context, keyNames[index]
                                    ),
                                    text: "Show",
                                    icon: Icons.remove_red_eye_outlined
                                )
                              ]
                                  : <Widget> [
                                bloc.indexToAdd == index
                                    ? SymbiotTextField(
                                  onChanged: (text) => bloc.newKey = text,
                                  onSubmitted: (text) {
                                    bloc.newKey = text;
                                    bloc.setKey(keyNames[index]);
                                  },
                                )
                                    : const SizedBox(),
                                Button(
                                    onTap: () => bloc.indexToAdd == index
                                        ? bloc.setKey(keyNames[index])
                                        : bloc.showTextfield(index),
                                    text: "Add",
                                    icon: Icons.send_outlined
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
    )
  );
}