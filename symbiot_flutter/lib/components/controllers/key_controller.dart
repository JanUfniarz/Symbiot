// ignore_for_file: curly_braces_in_flow_control_structures

import 'package:flutter/material.dart';

import '../../ui/widgets/key_popup.dart';
import '../command_executor.dart';
import '../connection/key_connector.dart';

class KeyController extends ChangeNotifier {
  CommandExecutor _executor;
  KeyConnector _connector;

  final String _path = "keys.txt";

  Map<String, String> _keys = {};

  Map<String, String> get keys => Map.from(_keys);

  int? indexToAdd;

  String? newKey;

  KeyController._private(this._executor, this._connector);
  static KeyController? _instance;

  factory KeyController.singleton({
    KeyConnector? connector,
    CommandExecutor? executor,
  }) {
    if (_instance != null) return _instance!;
    if (connector == null || executor == null)
      throw Exception("Provide Dependencies");
    _instance = KeyController._private(executor, connector);
    return _instance!;
  }

  void setKey(String name) {
    _keys[name] = newKey!;
    indexToAdd = null;
    newKey = null;
    notifyListeners();
    _saveKeys();
    distribute();
  }

  void distribute() async {
    await _getKeys();
    if (keys.isNotEmpty) _connector.provideKeys(keys);
    notifyListeners();
  }

  void clear(String name) {
    _connector.clearKey(name);
    _keys.remove(name);
    notifyListeners();
    _saveKeys();
  }

  void showTextfield(int index) {
    newKey = null;
    indexToAdd = index;
    notifyListeners();
  }

  void showKey(BuildContext context, String name) => showDialog(
      context: context,
      builder: (BuildContext context) => KeyPopup(
            name: name,
            apiKey: keys[name] ?? "No Key"));

  Future<void> _getKeys() async => await _executor
      // language=PowerShell
      .run("Get-Content $_path", return_: true)
      .then((content) => _keys = Map.fromEntries(RegExp(r'<(.*?)>')
          .allMatches(content)
          .map((match) => match.group(1))
          .toList()
          .map((el) => MapEntry(
      el!.split("=")[0], el.split("=")[1]))));

  void _saveKeys() => _executor.run(
      // language=PowerShell
      "Set-Content -Path $_path -Value \"${_keys.entries
          .map((en) => "<${en.key}=${en.value}>").join()}\"");
}
