import 'package:flutter/material.dart';

import '../palette.dart';

class SymbiotScaffold extends StatelessWidget {

  final String tittle;
  final Widget? body;

  const SymbiotScaffold({super.key, String? tittle, this.body}):
      tittle = tittle ?? "Symbiot";

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
  );
}