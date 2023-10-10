import 'package:symbiot_flutter/models/record_model.dart';

import 'message_model.dart';

class ChatModel {
  final int stepID;
  final String status;
  final List<MessageModel> messages;

  ChatModel(RecordModel step):
        stepID = step.id,
        status = step.status,
        messages = (step.body ?? "")
            .split("<@entry>")
            .sublist(1)
            .expand((el) {
              var split = el.split("<@time>");
              String time = split[0];
              split = split[1].split("<@res>");
              return [MessageModel(split[0], Role.user, time),
                      MessageModel(split[1], Role.assistant, time)];
            }).toList();
}
