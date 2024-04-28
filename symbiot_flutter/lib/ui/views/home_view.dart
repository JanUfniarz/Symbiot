import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/ui/style/style_provider.dart';

import '../../components/controllers/main_operation_controller.dart';
import '../style/palette.dart';
import '../widgets/input_bar.dart';
import '../widgets/operation_card.dart';
import '../widgets/operations_gallery.dart';

class HomeView extends StatelessWidget{
  const HomeView({super.key});

  @override
  Widget build(BuildContext context) =>
      Consumer<MainOperationController>(
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

                    Text(
                      "Type what you want the program to do!",
                      style: StyleProvider.header1,
                    ),

                    const SizedBox(height: 20),

                    OperationsGallery(
                      primary: Palette.accent,
                      operationsCards: List.generate(
                        controller.cache.operations.length, (index) =>
                          OperationCard(
                            name: controller.cache.operations[index].name,
                            onTap: () => controller.openOperation(
                                controller.cache.operations[index].id,
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