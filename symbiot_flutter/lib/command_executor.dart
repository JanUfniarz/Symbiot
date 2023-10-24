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


  Future<dynamic> run(String command,
      {bool return_ = false}) async {

    final result = await Process.run(_executable, _arguments + [command]);

    if (result.exitCode == 0) {
      print('Command $_executable executed correctly:'
          '\ncommand: $command'
          '\noutput: ${result.stdout}');

      if (return_) return result.stdout;

    } else {
      print('Error executing command $_executable:'
          '\ncommand: $command'
          '\noutput: ${result.stderr}');
      if (return_) throw Exception(result.stderr);
    }
  }
}