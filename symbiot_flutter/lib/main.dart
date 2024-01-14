import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/ui/symbiot_app.dart';

import 'components/command_executor.dart';
import 'components/connection/chat_connector.dart';
import 'components/connection/key_connector.dart';
import 'components/connection/operation_connector.dart';
import 'components/controllers/key_controller.dart';
import 'components/controllers/operation_controller.dart';


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