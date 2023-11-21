import 'package:flutter/material.dart';
import 'package:symbiot_flutter/ui/widgets/input_bar.dart';

import '../style/palette.dart';

class SymbiotScaffold extends StatelessWidget {

  final String tittle;
  final Widget? body;
  final void Function(String)? onSend;

  const SymbiotScaffold({
    super.key,
    this.tittle = "Symbiot",
    this.body,
    this.onSend});


  @override
  Widget build(BuildContext context) => Scaffold(
    backgroundColor: Palette.background,

    appBar: PreferredSize(
      preferredSize: const Size.fromHeight(30),
      child: AppBar(
        backgroundColor: Palette.accent,
        title: Text(
          tittle,
          style: const TextStyle(
            color: Palette.background,
          ),
        ),
        centerTitle: true,
      ),
    ),

    body: body,

    bottomNavigationBar: onSend == null ? null

        : ClipRRect(
          borderRadius: const BorderRadius.only(
            topLeft: Radius.circular(24),
            topRight: Radius.circular(24),
          ),
          child: Container(
            color: Palette.backgroundGrey,
            padding: const EdgeInsets.all(20),
            child: InputBar(onSend: onSend!),
          ),
        )

  );
}