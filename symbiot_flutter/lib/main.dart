import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/command_executor.dart';
import 'package:symbiot_flutter/connection/key_connector.dart';
import 'package:symbiot_flutter/symbiot_app.dart';
import 'package:symbiot_flutter/views/keys_view.dart';

import 'connection/operation_connector.dart';
import 'managers/key_manager.dart';
import 'managers/operation_manager.dart';
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

  KeyManager.getInstance(
    connector: KeyConnector(),
    executor: CommandExecutor.powerShell(),
  ).distribute();

  OperationManager.getInstance(
    connector: OperationConnector(),
  ); // TODO: get

  runApp(MaterialApp(home: SymbiotApp()));
}