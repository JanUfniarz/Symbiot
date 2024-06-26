import 'package:flutter/material.dart';

import '../style/palette.dart';

class SymbiotDivider extends StatelessWidget {
  const SymbiotDivider({super.key});

  @override
  Widget build(BuildContext context) => const Padding(
    padding: EdgeInsets.symmetric(horizontal: 60),
    child: Divider(
      color: Palette.primary,
      thickness: 2,
    ),
  );
}
