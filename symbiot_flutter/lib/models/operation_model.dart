class OperationModel {


  String? _leafSummary;
  String get leafSummary => _leafSummary ?? "No leaf summary";
  set leafSummary(String value) => _leafSummary = value;


  String? _body;
  String get body => _body ?? "No body";
  set body(String value) => _body = value;


  String get status => _status ?? "No status";
  String? _status;
  set status(String value) => _status = value;


  List<int>? _links;
  List<int> get links => _links ?? [];
  set links(List<int> value) => _links = value;


  List<int>? _branches;
  List<int> get branches => _branches ?? [];
  set branches(List<int> value) => _branches = value;


  String? _wish;
  String get wish => _wish ?? "No wish";
  set wish(String value) => _wish = value;


  String? _name;
  String get name => _name ?? "No name";
  set name(String value) => _name = value;


  int? _id;
  int get id => _id ?? -1;
  set id(int value) => _id = value;

  BigO? bigO;


  OperationModel(this._id, this._name,
      this._wish, this._branches, this._links,
      this._status, this._body, this._leafSummary
      );

  OperationModel.fromJson(dynamic data) {
    _id = data["id"];
    _name = data["name"];
    _wish = data["wish"];
    _branches = data["branches"];
    _links = data["links"];
    _status = data["status"];
    _body = data["body"];
    _leafSummary = data["leafSummary"];
  }
}


enum BigO {
  n, n2
}
