// ignore_for_file: avoid_print

import 'dart:io';

class CommandExecutor {

  final String _executable;
  final List<String> _arguments;

  CommandExecutor.powerShell():
        _executable = "powershell",
        _arguments = ["-NoProfile", "-NonInteractive"];

  CommandExecutor.python():
        _executable = "python",
        _arguments = ["-c"];


  Future<void> runCommand(String? command) async {

    if (command == null) {
      print("runCommand - No command");
      return;
    }
    final result = await Process.run(
        _executable, _arguments + [command]
    );

    if (result.exitCode == 0) {
      print('Komenda $_executable wykonana poprawnie:');
      print(result.stdout);
    } else {
      print('Błąd podczas wykonywania komendy $_executable:');
      print(result.stderr);
    }
  }

}