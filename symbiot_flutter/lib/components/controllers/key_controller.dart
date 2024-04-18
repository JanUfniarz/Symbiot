import 'package:flutter/material.dart';

import '../../ui/widgets/key_popup.dart';
import '../command_executor.dart';
import '../connection/key_connector.dart';

class KeyController extends ChangeNotifier {
  final CommandExecutor _executor;
  final KeyConnector _connector;

  final String _path;
  Map<String, String> _keys;

  int? indexToAdd;
  String? newKey;

  KeyController(this._executor, this._connector, {path = "keys.txt"})
      : _path = path,
        _keys = {} {
    distribute();
  }

  Map<String, String> get keys => Map.from(_keys);

  void setKey(String name) {
    _keys[name] = newKey!;
    indexToAdd = null;
    newKey = null;
    notifyListeners();
    _saveKeys();
    distribute();
  }

  Future<void> distribute() async {
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
      apiKey: keys[name] ?? "No Key")
  );

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
