import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/ui/widgets/symbiot_scaffold.dart';

import '../../bloc/controllers/operation_controller.dart';
import '../../models/chat_model.dart';
import '../../models/message_model.dart';
import '../palette.dart';

class ChatView extends StatelessWidget {
  final String stepID;

  final double _messageCornerRadius = 20;

  const ChatView(this.stepID, {super.key});

  ChatModel _model(OperationController controller) => ChatModel(controller.record(stepID));

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
              ),
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
            }).toList(),
          ),
      ),
  );
}