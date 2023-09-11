import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/widgets/symbiot_text_field.dart';

import '../BLoCs/operation_bloc.dart';
import '../palette.dart';

class HomeView extends StatelessWidget {
  const HomeView({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer<OperationBloc>(
      builder: (context, bloc, child) =>
          Padding(
            padding: const EdgeInsets.all(10),
            child: Column(
              children: <Widget>[

                const Text(
                  "Type what you want the program to do!",
                  style: TextStyle(
                    color: Palette.primary,
                    fontSize: 30,
                  ),
                ),

                const SizedBox(height: 20),

                SymbiotTextField(
                  onChanged: (text) {},
                  hintText: "Wish",
                ),


              ],
            ),
          ),
    );
  }
}
