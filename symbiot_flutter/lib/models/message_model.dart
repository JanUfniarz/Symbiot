class MessageModel {
  final String content;
  final Role role;
  final DateTime time;

  MessageModel(this.content, this.role, String time):
        time = DateTime.parse(time);
}

enum Role {
  user, assistant, server, error,
}