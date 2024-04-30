import 'package:flutter/material.dart';

import '../../ui/widgets/key_popup.dart';
import '../command_executor.dart';
import '../connection/key_connector.dart';
import '../internal_cache.dart';

class KeyController extends ChangeNotifier {
  final CommandExecutor _executor;
  final KeyConnector _connector;
  final InternalCache cache;

  final String _path;

  int? indexToAdd;
  String? newKey;

  KeyController(
      this._executor, this._connector, this.cache,
      {path = "keys.txt"}
      ): _path = path {
    distribute();
  }

  Map<String, String> get keys => Map.from(cache.keys);

  void setKey(String name) {
    cache.keys[name] = newKey!;
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
    cache.keys.remove(name);
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
      .then((content) => cache.keys = Map.fromEntries(RegExp(r'<(.*?)>')
          .allMatches(content)
          .map((match) => match.group(1))
          .toList()
          .map((el) => MapEntry(
      el!.split("=")[0], el.split("=")[1]))));

  void _saveKeys() => _executor.run(
      // language=PowerShell
      "Set-Content -Path $_path -Value \"${cache.keys.entries
          .map((en) => "<${en.key}=${en.value}>").join()}\"");
}
