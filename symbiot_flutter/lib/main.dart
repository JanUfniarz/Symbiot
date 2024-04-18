import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/ui/symbiot_app.dart';

import 'components/command_executor.dart';
import 'components/connection/chat_connector.dart';
import 'components/connection/key_connector.dart';
import 'components/connection/operation_connector.dart';
import 'components/controllers/key_controller.dart';
import 'components/controllers/operation_controller.dart';

void main() => runApp(SymbiotApp(providers: [
  ChangeNotifierProvider<KeyController>.value(
    value: KeyController(
        CommandExecutor.powerShell(),
        KeyConnector()
    ),
  ),
  ChangeNotifierProvider<OperationController>.value(
    value: OperationController(
      OperationConnector(),
      ChatConnector(),
    ),
  ),
]));