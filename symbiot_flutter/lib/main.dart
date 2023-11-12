import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/connection/key_connector.dart';
import 'package:symbiot_flutter/ui/symbiot_app.dart';

import 'bloc/command_executor.dart';
import 'bloc/controllers/key_controller.dart';
import 'bloc/controllers/operation_controller.dart';
import 'connection/chat_connector.dart';
import 'connection/operation_connector.dart';

void main() async {

  KeyController keyController = KeyController
      .getInstance(
    connector: KeyConnector(),
    executor: CommandExecutor.powerShell()
  );

  keyController.distribute();

  OperationController operationController = OperationController
      .getInstance(
    operationConnector: OperationConnector(),
    chatConnector: ChatConnector(),
  );

  await operationController.loadData();

  runApp(MultiProvider(
      providers: [
        ChangeNotifierProvider<KeyController>.value(
          value: keyController,
        ),
        ChangeNotifierProvider<OperationController>.value(
          value: operationController,
        ),
      ],
      child: const MaterialApp(home: SymbiotApp()),
  ));
}