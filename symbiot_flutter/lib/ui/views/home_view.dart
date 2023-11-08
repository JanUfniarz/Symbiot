import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../bloc/controllers/operation_controller.dart';
import '../palette.dart';
import '../widgets/input_bar.dart';
import '../widgets/operation_card.dart';
import '../widgets/operations_gallery.dart';

class HomeView extends StatelessWidget{
  const HomeView({super.key});

  @override
  Widget build(BuildContext context) =>
      Consumer<OperationController>(
        builder: (context, controller, child) =>
            Container(
              alignment: Alignment.topCenter,
              child: Padding(
                padding: const EdgeInsets.all(10),
                child: Column(
                  children: <Widget>[

                    InputBar(
                      onSend: (text) => controller.newOperation(text)
                          .then((val) => controller.openChat(
                          val.records.first, context)),
                    ),

                    const Text(
                      "Type what you want the program to do!",
                      style: TextStyle(
                        color: Palette.primary,
                        fontSize: 30,
                      ),
                    ),

                    const SizedBox(height: 20),

                    OperationsGallery(
                      primary: Palette.accent,
                      operationsCards: List.generate(
                        controller.models.length, (index) =>
                          OperationCard(
                            name: controller.models[index].name,
                            onTap: () => controller.openOperation(
                                controller.models[index].id,
                                context
                            ),
                          ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
      );
}