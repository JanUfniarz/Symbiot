import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/ui/style/style_provider.dart';
import 'package:symbiot_flutter/ui/widgets/symbiot_scaffold.dart';

import '../../components/controllers/chat_controller.dart';
import '../../models/chat_model.dart';
import '../../models/message_model.dart';
import '../style/palette.dart';
import '../widgets/message.dart';

class ChatView extends StatefulWidget {
  final String stepID;

  const ChatView(this.stepID, {super.key});

  @override
  State<ChatView> createState() => _ChatViewState();
}

class _ChatViewState extends State<ChatView> {
  @override
  void initState() {
    super.initState();
    Provider.of<ChatController>(context, listen: false).openChat(widget.stepID);
  }

  @override
  void dispose() {
    Provider.of<ChatController>(context, listen: false).closeChat();
    super.dispose();
  }

  ChatModel _model(ChatController controller) =>
      ChatModel(controller.record(widget.stepID));

  String _date(MessageModel model) {
    String date = model.time.toString();
    return date.substring(0, date.length -7);
  }

  @override
  Widget build(BuildContext context) => Consumer<ChatController>(
      builder: (context, controller, child) => SymbiotScaffold(
          onSend: (text) => controller.chat(text, widget.stepID),
          body: ListView(

            children: _model(controller).messages.asMap().entries.expand((entry) {
              int index = entry.key;
              MessageModel messageModel = entry.value;
              String date = _date(messageModel);
              String previousDate = "";
              try {
                previousDate = _date(
                    _model(controller).messages[index - 1]);
              } catch (_) {/* RangeError pass */}

              return [
                date == previousDate ? const SizedBox() : Center(
                  child: Text(date,
                    style: StyleProvider.date,
                  ),
                ),

                Message(messageModel,
                  delete: () => controller.deleteMessage(widget.stepID, index),
                  change: () => controller.changeMessage(widget.stepID, index, context),
                )
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