import 'package:flutter/material.dart';
import 'package:symbiot_flutter/connection/key_connector.dart';

import '../command_executor.dart';
import '../widgets/key_popup.dart';

class KeyManager extends ChangeNotifier {

  final CommandExecutor _executor;
  final KeyConnector _connector;

  final String _path = "keys.txt";

  Map<String, String> _keys = {};
  Map<String, String> get keys => Map.from(_keys);

  int? indexToAdd;

  String? newKey;

  KeyManager(this._executor, this._connector);

  void setKey(String name) {
    _keys[name] = newKey!;
    indexToAdd = null;
    newKey = null;
    notifyListeners();
    _saveKeys();
  }

  void distribute() async {
    await _getKeys();
    _connector.provideKeys(keys);
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

  void showKey(BuildContext context, name) => showDialog(
      context: context,
      builder: (BuildContext context) => KeyPopup(
        name: name,
        apiKey: keys[name] ?? "No Key",
      )
  );

    Future<void> _getKeys() async =>
        await _executor.run(
            "Get-Content $_path",
            return_: true
        ).then((content) => _keys = Map
            .fromEntries(RegExp(r'<(.*?)>')
            .allMatches(content)
            .map((match) => match.group(1))
            .toList().map((el) => MapEntry(
            el!.split("=")[0], el.split("=")[1]
        ))));

    void _saveKeys() => _executor.run(
        "Set-Content -Path $_path -Value \"${
            _keys.entries.map(
                    (en) => "<${en.key}=${en.value}>"
            ).join()}\"");
}