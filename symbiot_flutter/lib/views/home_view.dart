import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/widgets/operation_card.dart';
import 'package:symbiot_flutter/widgets/operations_gallery.dart';

import '../controllers/operation_controller.dart';
import '../palette.dart';

class HomeView extends StatelessWidget {
  const HomeView({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer<OperationController>(
      builder: (context, bloc, child) =>
          Expanded(
            child: Stack(
              children: <Widget>[

                Container(
                  alignment: Alignment.topCenter,
                  child: Padding(
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

                        Consumer<OperationController>(
                          builder: (context, controller, child) =>
                              OperationsGallery(
                            primary: Palette.accent,
                            operationsCards: [
                              OperationCard(
                                name: "name",
                                onTap: () {},
                                refresh: () {}
                              )
                            ],
                          ),
                        )

                      ],
                    ),
                  ),
                ),

                Container(
                  alignment: Alignment.bottomCenter,
                  padding: const EdgeInsets.symmetric(
                      horizontal: 70,
                      vertical: 20
                  ),
                  child: Row(
                    children: <Widget>[

                      Flexible(
                        child: TextField(
                          decoration: const InputDecoration(
                            filled: true,
                            fillColor: Palette.accent,
                            hintText: 'Wpisz wiadomość...',
                          ),
                          onChanged: (text) {},
                          onSubmitted: (text) {},
                          maxLines: null,
                        ),
                      ),

                      IconButton(
                        iconSize: 30,
                        color: Palette.primary,
                        icon: const Icon(Icons.send),
                        onPressed: () {},
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
    );
  }
}
