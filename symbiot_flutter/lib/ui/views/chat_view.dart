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

  const ChatView(this.stepID, {super.key});

  @override
  Widget build(BuildContext context) => Consumer<OperationController>(
      builder: (context, controller, child) {
        ChatModel model = ChatModel(controller.record(stepID));
        return SymbiotScaffold(
          body: SingleChildScrollView(
            child: Column(

              children: List.generate(model.messages.length, (index) {
                MessageModel mesModel = model.messages[index];
                // ignore: unnecessary_cast
                return Card(
                  elevation: 0,
                  color: Palette.background,
                  child: Padding(
                    padding: const EdgeInsets.symmetric(vertical: 10),
                    child: Row(
                      mainAxisAlignment: mesModel.axisAlignment,
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: <Widget>[

                        Flexible(
                          child: ClipRRect(
                            borderRadius: const BorderRadius.only(
                              topLeft: Radius.circular(16),
                              topRight: Radius.circular(16),
                            ),

                            child: Container(
                              padding: const EdgeInsets.all(20),
                              color: mesModel.color,
                              child: Text(mesModel.content,
                                textAlign: mesModel.textAlignment,
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
                ) as Widget;
              }) + [
                InputBar(
                  onSend: (text) => controller.chat(text, stepID)
              )],
            ),
          ),
        );
      });
}