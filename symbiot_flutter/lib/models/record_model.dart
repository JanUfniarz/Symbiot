class RecordModel {
  final String id;
  final RecordType type;
  dynamic previous;
  final String? path;
  final String? bigO;
  final List<dynamic> inputs;
  final List<dynamic>? outputs;
  String? body;
  final String status;

  RecordModel(json):
        id = json["id"],
        type = RecordType.values
            .firstWhere(
                (e) => e.toString() == 'RecordType.${json["type"]}'
        ),
        path = json["path"],
        bigO = json["bigO"],
        inputs = (json["inputs"] as List<dynamic>),
        outputs = (json["outputs"] as List<dynamic>),
        body = json["body"],
        status = json["status"],
        previous = json["previous"];
}

enum RecordType {
  script,
  step,
}