import 'package:flutter/material.dart';
import 'package:flutter_chat_types/flutter_chat_types.dart' as types;
import 'package:flutter_chat_ui/flutter_chat_ui.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/models/chat_model.dart';
import 'package:symbiot_flutter/widgets/symbiot_scaffold.dart';

import '../controllers/operation_controller.dart';
import '../models/message_model.dart';
import '../widgets/input_bar.dart';

class ChatView extends StatelessWidget {
  const ChatView({super.key});

  @override
  Widget build(BuildContext context) =>
      Consumer<OperationController>(builder: (context, controller, child) {
        ChatModel chatModel = ChatModel(controller.openedRecord!);
        return SymbiotScaffold(
            body: Column(children: <Widget>[
          InputBar(
            child: Chat(
              messages: List.generate(chatModel.messages.length, (index) {
                MessageModel messageModel = chatModel.messages[index];
                return types.TextMessage(
                  author: types.User(
                      id: messageModel.role.toString(),
                      firstName: messageModel.role.toString()),
                  id: '',
                  text: messageModel.content,
                  createdAt: messageModel.time.millisecondsSinceEpoch,
                );
              }),
              onSendPressed: (PartialText) {},
              user: const types.User(id: "user"),2
            ),
          )
        ]));
      });
}
