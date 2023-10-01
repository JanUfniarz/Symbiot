import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/widgets/operation_card.dart';
import 'package:symbiot_flutter/widgets/operations_gallery.dart';

import '../controllers/operation_controller.dart';
import '../palette.dart';
import '../widgets/input_bar.dart';

class HomeView extends StatelessWidget {
  const HomeView({super.key});

  @override
  Widget build(BuildContext context) =>
      Consumer<OperationController>(
        builder: (context, bloc, child) =>
          InputBar(
            child: Container(
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
                        operationsCards: List.generate(
                            controller.models!.length, (index) =>
                          OperationCard(
                            name: controller.models![index].name,
                            before: () {
                              controller.pickedIndex = index;
                              print("pickedIndex: ${controller.pickedIndex}"
                                  "\nmodels: ${controller.models![index].name}");
                            },
                            after: () => controller.loadData(),
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
    );
}