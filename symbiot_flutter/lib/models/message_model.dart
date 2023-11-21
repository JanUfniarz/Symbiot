import 'package:flutter/material.dart';
import 'package:symbiot_flutter/ui/style/palette.dart';

class MessageModel {
  final String content;
  final Role role;
  final DateTime time;

  MessageModel(this.content, this.role, String time):
        time = DateTime.parse(time);

  MainAxisAlignment get axisAlignment {
    switch (role) {
      case Role.user: return MainAxisAlignment.end;
      case Role.assistant: return MainAxisAlignment.start;
      case Role.function:
      case Role.error: return MainAxisAlignment.center;
    }
  }

  TextAlign get textAlignment {
    switch (role) {
      case Role.user: return TextAlign.end;
      case Role.assistant: return TextAlign.start;
      case Role.function:
      case Role.error: return TextAlign.center;
    }
  }

  Color get color {
    switch (role) {
      case Role.user: return Palette.primary;
      case Role.assistant: return Palette.accent;
      case Role.function: return Palette.infoYellow;
      case Role.error: return Palette.delete;
    }
  }
}

enum Role {
  user, assistant, function, error,
}