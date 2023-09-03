// ignore_for_file: curly_braces_in_flow_control_structures
// ignore_for_file: avoid_function_literals_in_foreach_calls

import 'container_model.dart';

class OperationModel {
  int id;
  String wish;
  String nordStar;
  String? leafSummaryStatus;
  String status;
  String name;
  String body;
  List<ContainerModel> containers;
  
  OperationModel(dynamic json):
        id = json["id"],
        wish = json["wish"],
        nordStar = json["nord_star"],
        leafSummaryStatus = json["leaf_summary_status"],
        status = json["status"],
        name = json["name"],
        body = json["body"],
        containers = (json["containers"] as List<dynamic>)
            .map((el) => ContainerModel(el))
            .toList() {
    for (ContainerModel container in containers)
      containers.forEach((element) {
        if (element.id == container.previous)
          container.previous = element;
      });
  }
}