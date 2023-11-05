import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/ui/widgets/input_bar.dart';
import 'package:symbiot_flutter/ui/widgets/symbiot_scaffold.dart';

import '../../bloc/controllers/operation_controller.dart';
import '../../models/chat_model.dart';
import '../widgets/message.dart';

class ChatView extends StatelessWidget {
  final String stepID;

  const ChatView(this.stepID, {super.key});

  @override
  Widget build(BuildContext context) => Consumer<OperationController>(
      builder: (context, controller, child) => SymbiotScaffold(
          body: SingleChildScrollView(
            child: Column(
              children: ChatModel(controller.record(stepID)).messages
                  // ignore: unnecessary_cast
                  .map((mes) => Message(mes) as Widget).toList() +
                  [InputBar(onSend: (text) => controller.chat(text, stepID))],
            ),
          ),
        ),
      );
}