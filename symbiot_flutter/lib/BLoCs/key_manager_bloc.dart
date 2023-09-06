import 'package:flutter/material.dart';
import 'package:symbiot_flutter/connection/key_connector.dart';

import '../command_executor.dart';

class KeyManager extends ChangeNotifier {

  final CommandExecutor _executor;
  final KeyConnector _connector;

  final String _path = "keys.txt";

  Map<String, String> _keys = {};
  Map<String, String> get keys => Map.from(_keys);

  KeyManager(this._executor, this._connector);

  void setKey(String name, String value) {
    _keys[name] = value;
    notifyListeners();
    saveKeys();
  }

  void getKeys() async =>
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

  void saveKeys() {
    String content = "";
    _keys.forEach((name, key) => content += "<$name=$key>");
    _executor.run(
        "Set-Content -Path $_path -Value $content"
    );
  }
}