class ContainerModel {
  int id;
  ContainerType type;
  ContainerModel? previous;
  String? path;
  String? bigO;
  List<dynamic> inputs;
  List<dynamic>? outputs;
  String? body;
  String status;

  ContainerModel(dynamic json, this.previous):
        id = json["id"],
        type = ContainerType.values
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
        status = json["status"];
}

enum ContainerType {
  script,
  step,
}


