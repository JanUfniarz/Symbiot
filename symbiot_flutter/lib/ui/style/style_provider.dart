import 'package:flutter/material.dart';
import 'package:symbiot_flutter/ui/style/palette.dart';

class StyleProvider {
  static TextStyle date = TextStyle(
      color: Palette.lightGrey,
      fontWeight: FontWeight.bold,
      fontSize: 12
  );

  static TextStyle header1 = const TextStyle(
    color: Palette.primary,
    fontSize: 30,
  );

  static TextStyle text1 = const TextStyle(
    color: Palette.accent,
    fontSize: 20,
  );
}