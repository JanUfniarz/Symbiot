import 'package:flutter/material.dart';
import 'package:symbiot_flutter/ui/style/palette.dart';


class SymbiotTextField extends StatelessWidget {
  const SymbiotTextField({
    super.key,
    this.hintText,
    required this.onChanged,
    this.onSubmitted
  });

  final String? hintText;
  final void Function(String) onChanged;
  final void Function(String)? onSubmitted;

  @override
  Widget build(BuildContext context) => Row(
    mainAxisAlignment: MainAxisAlignment.center,
    children: <Widget>[

     SizedBox(
       width: 450,
       child: TextField(
         onChanged: onChanged,
         onSubmitted: onSubmitted,
         decoration: InputDecoration(
           filled: true,
           fillColor: Palette.accent,
           hintText: hintText,
         ),
        ),
      ),
    ],
  );
}