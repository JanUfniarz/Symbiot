import 'package:flutter/material.dart';
import 'package:flutter_chat_types/flutter_chat_types.dart' as types;
import 'package:flutter_chat_ui/flutter_chat_ui.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/models/chat_model.dart';
import 'package:symbiot_flutter/widgets/symbiot_scaffold.dart';

import '../controllers/operation_controller.dart';
import '../models/message_model.dart';

class ChatView extends StatelessWidget {
  const ChatView({super.key});

  @override
  Widget build(BuildContext context) =>
      Consumer<OperationController>(builder: (context, controller, child) {
        ChatModel chatModel = ChatModel(controller.openedRecord!);
        return SymbiotScaffold(
            body: Chat(
              messages: List.generate(chatModel.messages.length, (index) {

                MessageModel messageModel = chatModel.messages[index];
                String role = messageModel.role
                    .toString().replaceAll("Role.", "");

                return types.TextMessage(
                  author: types.User(
                      id: role,
                      firstName: role
                  ),
                  id: '',
                  text: messageModel.content,
                  createdAt: messageModel.time.millisecondsSinceEpoch,
                );
              }).reversed.toList(),
              onSendPressed: (text) => controller.chat(text.text),
              user: const types.User(id: "user"),
            ));
      });
}
