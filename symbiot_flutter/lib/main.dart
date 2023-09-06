import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/command_executor.dart';
import 'package:symbiot_flutter/connection/key_connector.dart';
import 'package:symbiot_flutter/views/keys_view.dart';

import 'BLoCs/key_manager_bloc.dart';
import 'connection/operation_connector.dart';
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

void main() => runApp(MultiProvider(
    providers: [
      ChangeNotifierProvider<KeyManager>.value(
          value: KeyManager(
              CommandExecutor.powerShell(),
              KeyConnector()
          )
      ),
    ],
    child: const MaterialApp(home: KeysView())));