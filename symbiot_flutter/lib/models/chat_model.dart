import 'dart:convert';

import 'package:symbiot_flutter/models/record_model.dart';

import 'message_model.dart';

class ChatModel {
  final String stepID;
  final String status;
  final List<MessageModel> messages;

  ChatModel(RecordModel step):
        stepID = step.id,
        status = step.status,
        messages = (step.body ?? "")
            .split("<@entry>")
            .sublist(1)
            .map((el) => json.decode(el) as Map<String, dynamic>)
            .map((el) => MessageModel(
              el["content"]!,
              Role.values.firstWhere(
                      (role) => role.toString() == 'Role.${el["role"]}'),
              el["time"]!))
            .toList();
}
