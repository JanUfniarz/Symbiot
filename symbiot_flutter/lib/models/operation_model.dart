import 'record_model.dart';

class OperationModel {
  final String id;
  final String wish;
  final String nordStar;
  final String? leafSummaryStatus;
  final String status;
  final String name;
  final String body;
  List<RecordModel> records;
  
  OperationModel(json):
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
      records.forEach((element) =>
        element.id == record.previous
            ? record.previous = element : null);
  }
}