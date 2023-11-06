import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/ui/widgets/input_bar.dart';
import 'package:symbiot_flutter/ui/widgets/symbiot_scaffold.dart';

import '../../bloc/controllers/operation_controller.dart';
import '../../models/chat_model.dart';
import '../../models/message_model.dart';
import '../palette.dart';

class ChatView extends StatelessWidget {
  final String stepID;

  final double _messageCornerRadius = 20;

  const ChatView(this.stepID, {super.key});

  @override
  Widget build(BuildContext context) => Consumer<OperationController>(
      builder: (context, controller, child) => SymbiotScaffold(
          body: SingleChildScrollView(
            child: Column(

              children: ChatModel(controller.record(stepID)).messages
                    // ignore: unnecessary_cast
                    .map((mes) => Card(
                  elevation: 0,
                  color: Palette.background,
                  child: Padding(
                    padding: const EdgeInsets.symmetric(vertical: 10),
                    child: Row(
                      mainAxisAlignment: mes.axisAlignment,
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: <Widget>[

                        Flexible(
                          child: ClipRRect(
                            borderRadius: BorderRadius.only(
                              topLeft: Radius.circular(_messageCornerRadius),
                              topRight: Radius.circular(_messageCornerRadius),
                              bottomLeft: Radius.circular(
                                  mes.role == Role.assistant ? 0 : _messageCornerRadius
                              ),
                              bottomRight: Radius.circular(
                                  mes.role == Role.user ? 0 : _messageCornerRadius
                              ),
                            ),

                            child: Container(
                              padding: const EdgeInsets.all(20),
                              color: mes.color,
                              child: Text(mes.content,
                                textAlign: mes.textAlignment,
                                style: const TextStyle(
                                    color: Palette.background,
                                    fontSize: 20,
                                    backgroundColor: Colors.transparent,
                                    height: 1
                                ),
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ) as Widget
              ).toList() + [
                InputBar(
                  onSend: (text) => controller.chat(text, stepID)
              )],
            ),
          ),
      )
  );
}