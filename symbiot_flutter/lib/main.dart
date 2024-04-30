import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/components/controllers/chat_controller.dart';
import 'package:symbiot_flutter/ui/symbiot_app.dart';

import 'components/command_executor.dart';
import 'components/connection/chat_connector.dart';
import 'components/connection/key_connector.dart';
import 'components/connection/operation_connector.dart';
import 'components/controllers/key_controller.dart';
import 'components/controllers/main_operation_controller.dart';
import 'components/internal_cache.dart';

void main() {
  InternalCache cache = InternalCache();
  OperationConnector operationConnector = OperationConnector();

  runApp(SymbiotApp(providers: [
    ChangeNotifierProvider<KeyController>.value(
      value: KeyController(
        CommandExecutor.powerShell(),
        KeyConnector(),
        cache
      ),
    ),
    ChangeNotifierProvider<MainOperationController>.value(
      value: MainOperationController(
        operationConnector,
        cache
      ),
    ),
    ChangeNotifierProvider<ChatController>.value(
      value: ChatController(
        operationConnector,
        cache,
        ChatConnector()
      )
    )
]));
}