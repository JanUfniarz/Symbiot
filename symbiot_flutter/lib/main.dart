import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/command_executor.dart';
import 'package:symbiot_flutter/connection/key_connector.dart';
import 'package:symbiot_flutter/symbiot_app.dart';

import 'connection/operation_connector.dart';
import 'controllers/key_controller.dart';
import 'controllers/operation_controller.dart';

// void main() {
//
//   runApp(MaterialApp(
//     home: HomeView(
//       connector: FirstConnector(),
//     ),
//   ));
// }

// void main() => runApp(MaterialApp(
//   home: ApiControlPanel(
//     connector: OperationConnector(),
//   ),
// ));

void main() async {

  KeyController keyController = KeyController
      .getInstance(
    connector: KeyConnector(),
    executor: CommandExecutor.powerShell()
  );

  keyController.distribute();

  OperationController operationController = OperationController
      .getInstance(
    connector: OperationConnector(),
  );

  await operationController.loadData();

  runApp(MultiProvider(
      providers: [
        ChangeNotifierProvider<KeyController>.value(
          value: KeyController.getInstance(),
        ),
        ChangeNotifierProvider<OperationController>.value(
          value: OperationController.getInstance(),
        ),
      ],
      child: const MaterialApp(home: SymbiotApp()),
  ));
}