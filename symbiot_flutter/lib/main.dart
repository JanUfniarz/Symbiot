import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/command_executor.dart';
import 'package:symbiot_flutter/connection/key_connector.dart';
import 'package:symbiot_flutter/symbiot_app.dart';
import 'package:symbiot_flutter/views/keys_view.dart';

import 'connection/operation_connector.dart';
import 'controllers/key_controller.dart';
import 'controllers/operation_controller.dart';
import 'tests/api_control_panel.dart';

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

void main() {

  KeyController.getInstance(
    connector: KeyConnector(),
    executor: CommandExecutor.powerShell(),
  ).distribute();

  OperationController.getInstance(
    connector: OperationConnector(),
  ); // TODO: get

  runApp(MaterialApp(home: SymbiotApp()));
}