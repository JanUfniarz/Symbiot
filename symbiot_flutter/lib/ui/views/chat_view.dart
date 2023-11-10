import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/ui/widgets/symbiot_scaffold.dart';

import '../../bloc/controllers/operation_controller.dart';
import '../../models/chat_model.dart';
import '../../models/message_model.dart';
import '../palette.dart';
import '../widgets/message.dart';

class ChatView extends StatelessWidget {
  final String stepID;

  const ChatView(this.stepID, {super.key});

  ChatModel _model(OperationController controller) =>
      ChatModel(controller.record(stepID));

  String _date(MessageModel model) {
    String date = model.time.toString();
    return date.substring(0, date.length -7);
  }

  @override
  Widget build(BuildContext context) => Consumer<OperationController>(
      builder: (context, controller, child) => SymbiotScaffold(
          onSend: (text) => controller.chat(text, stepID),
          body: ListView(

            children: _model(controller).messages
                  .map((messageModel) => Message(messageModel)
            ).toList().asMap().entries.expand((entry) {
              String date = _date(_model(controller).messages[entry.key]);
              String previousDate = "";
              try {
                previousDate = _date(
                    _model(controller).messages[entry.key - 1]);
              } catch (ig) {/* RangeError pass */}

              return [
                date == previousDate ? const SizedBox() : Center(
                  child: Text(date,
                    style: TextStyle(
                      color: Palette.lightGrey,
                      fontWeight: FontWeight.bold,
                      fontSize: 12
                    ),
                  ),
                ),

                entry.value
              ];
            }).toList() + (!controller.trigger(get: true) ? [] : [const Center(
              child: CircularProgressIndicator(
                color: Palette.primary,
              ),
            )]),
          ),
      ),
  );
}