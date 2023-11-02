import 'package:flutter/material.dart';
import 'package:flutter_chat_types/flutter_chat_types.dart' as types;
import 'package:flutter_chat_ui/flutter_chat_ui.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/models/chat_model.dart';
import '../../control/controllers/operation_controller.dart';
import '../../models/message_model.dart';
import '../palette.dart';
import '../widgets/symbiot_scaffold.dart';

class ChatView extends StatelessWidget {

  final String recordID;

  const ChatView(this.recordID, {super.key});

  @override
  Widget build(BuildContext context) =>
      Consumer<OperationController>(builder: (context, controller, child) {
        ChatModel chatModel = ChatModel(controller.record(recordID));

        TextStyle messagesTextStyle = const TextStyle(
            color: Palette.background,
            fontWeight: FontWeight.bold,
            fontSize: 16
        );

        return SymbiotScaffold(
            body: Chat(
              theme: DarkChatTheme(
                backgroundColor: Palette.background,
                inputBackgroundColor: Palette.backgroundGrey,
                primaryColor: Palette.primary,
                secondaryColor: Palette.accent,
                sendButtonIcon: const Icon(
                  Icons.send,
                  color: Palette.primary,
                  size: 30,
                ),
                sentMessageBodyTextStyle: messagesTextStyle,
                receivedMessageBodyTextStyle: messagesTextStyle,
              ),

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
              onSendPressed: (text) => controller.chat(text.text, recordID),
              user: const types.User(id: "user"),
            ));
      });
}
