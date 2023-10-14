import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/controllers/operation_controller.dart';
import 'package:symbiot_flutter/views/chat_view.dart';
import 'package:symbiot_flutter/widgets/symbiot_divider.dart';

import '../palette.dart';
import '../widgets/input_bar.dart';
import '../widgets/symbiot_scaffold.dart';

class OperationView extends StatelessWidget {
  const OperationView({super.key});



  @override
  Widget build(BuildContext context) => Consumer<OperationController>(
        builder: (context, controller, child) => SymbiotScaffold(
          tittle: controller.model!.name,
          body: Column(
            children: [
              InputBar(
                onSend: (text) {}, // TODO: new step
                child: Align(
                  alignment: Alignment.topCenter,
                  child: SingleChildScrollView(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: <Widget>[
                        Padding(
                          padding: const EdgeInsets.symmetric(vertical: 10),
                          child: Text(
                            "The main purpose of this operation is:\n"
                            "${controller.model!.nordStar}",
                            style: const TextStyle(
                              color: Palette.accent,
                              fontSize: 25,
                            ),
                          ),
                        ),
                        const SymbiotDivider(),
                        Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: List.generate(
                              controller.model!.records.length,
                              (index) => InkWell(
                                    onTap: () => controller.openChat(
                                        controller.model!.records[index].id,
                                        context
                                    ),
                                    child: Card(
                                      child: Padding(
                                        padding: const EdgeInsets.all(20),
                                        child: Text(controller
                                            .model!.records[index].id
                                            .toString()),
                                      ),
                                    ),
                              )
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      );
}
