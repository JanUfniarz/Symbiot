class ContainerModel {
  int id;
  ContainerType type;
  ContainerModel? previous;
  String? path;
  String? bigO;
  List<dynamic> inputs;
  List<dynamic>? outputs;

}

enum ContainerType {
  script, step
}


