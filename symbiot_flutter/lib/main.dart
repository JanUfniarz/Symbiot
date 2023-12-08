import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/connection/key_connector.dart';
import 'package:symbiot_flutter/ui/symbiot_app.dart';

import 'bloc/command_executor.dart';
import 'bloc/controllers/key_controller.dart';
import 'bloc/controllers/operation_controller.dart';
import 'connection/chat_connector.dart';
import 'connection/operation_connector.dart';

void main() => runApp(MultiProvider(
      providers: [
        ChangeNotifierProvider<KeyController>.value(
          value: KeyController.getInstance(
              connector: KeyConnector(),
              executor: CommandExecutor.powerShell()
          ),
        ),
        ChangeNotifierProvider<OperationController>.value(
          value: OperationController.getInstance(
            operationConnector: OperationConnector(),
            chatConnector: ChatConnector(),
          ),
        ),
      ],
      child: const MaterialApp(home: SymbiotApp()),
  ));