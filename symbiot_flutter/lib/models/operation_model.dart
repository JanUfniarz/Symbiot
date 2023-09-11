// ignore_for_file: curly_braces_in_flow_control_structures
// ignore_for_file: avoid_function_literals_in_foreach_calls

import 'record_model.dart';

class OperationModel {
  int id;
  String wish;
  String nordStar;
  String? leafSummaryStatus;
  String status;
  String name;
  String body;
  List<RecordModel> records;
  
  OperationModel(dynamic json):
        id = json["id"],
        wish = json["wish"],
        nordStar = json["nord_star"],
        leafSummaryStatus = json["leaf_summary_status"],
        status = json["status"],
        name = json["name"],
        body = json["body"],
        records = (json["records"] as List<dynamic>)
            .map((el) => RecordModel(el))
            .toList() {
    for (RecordModel record in records)
      records.forEach((element) {
        if (element.id == record.previous)
          record.previous = element;
      });
  }
}