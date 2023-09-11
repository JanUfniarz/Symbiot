import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/tests/api_control_panel.dart';
import 'package:symbiot_flutter/views/home_view.dart';
import 'package:symbiot_flutter/views/keys_view.dart';
import 'package:symbiot_flutter/views/settings_view.dart';
import 'package:symbiot_flutter/widgets/bordered_button.dart';
import 'package:symbiot_flutter/widgets/symbiot_navigation_bar.dart';
import 'package:symbiot_flutter/widgets/symbiot_scaffold.dart';

import 'BLoCs/key_manager_bloc.dart';
import 'BLoCs/operation_bloc.dart';
import 'command_executor.dart';
import 'connection/key_connector.dart';
import 'connection/operation_connector.dart';

class SymbiotApp extends StatefulWidget {
  final List<ChangeNotifierProvider> providers;

  SymbiotApp({super.key}): providers = [
    ChangeNotifierProvider<KeyManager>.value(
      value: KeyManager.getInstance(),
    ),
    ChangeNotifierProvider<OperationBloc>.value(
        value: OperationBloc.getInstance(),
    ),
  ];

  @override
  State<SymbiotApp> createState() => _SymbiotAppState();
}

class _SymbiotAppState extends State<SymbiotApp> {
  int selected = 0;

  Widget _body(int selected) {
    switch (selected) {
      case 0: return const HomeView();
      case 1: return const KeysView();
      case 2: return const SettingsView();
      default: throw Exception("Wrong selected value");
    }
  }

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: widget.providers,
      child: SymbiotScaffold(
        tittle: SymbiotNavigationBar.labels[selected],
        body: Column(
          children: <Widget>[
            SymbiotNavigationBar(
              selected: selected,
              onSelect: (index) => setState(
                      () => selected = index),
            ),
            //? ======= test ============
            // TODO: remove when not needed
            const SizedBox(height: 20),
            BorderedButton(
              onTap: () => Navigator.of(context).push(
                  MaterialPageRoute(
                      builder: (context) => ApiControlPanel(
                          connector: OperationConnector()
                      )
                  )
              ),
              icon: Icons.api_outlined,
              text: "Control\nPanel",
            ),
            //? =========================
            _body(selected),
          ],
        ),
      ),
    );
  }
}