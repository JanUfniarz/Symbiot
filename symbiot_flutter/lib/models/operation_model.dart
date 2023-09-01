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
    containers = List.generate(
        (json["containers"] as List<dynamic>).length,
            (index) => ContainerModel(json["containers"][index])
    );
}