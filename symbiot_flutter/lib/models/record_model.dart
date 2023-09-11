class RecordModel {
  int id;
  RecordType type;
  dynamic previous;
  String? path;
  String? bigO;
  List<dynamic> inputs;
  List<dynamic>? outputs;
  String? body;
  String status;

  RecordModel(dynamic json):
        id = json["id"],
        type = RecordType.values
            .firstWhere(
                (e) => e.toString() == 'ContainerType.${json["type"]}'
        ),
        path = json["path"],
        bigO = json["bigO"],
        inputs = (json["inputs"] as List<dynamic>)
            .map((e) => e["data"]).toList(),
        outputs = (json["outputs"] as List<dynamic>)
            .map((e) => e["data"]).toList(),
        body = json["body"],
        status = json["status"],
        previous = json["previous"];
}

enum RecordType {
  script,
  step,
}