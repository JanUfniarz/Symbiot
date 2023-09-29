import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/tests/api_control_panel.dart';
import 'package:symbiot_flutter/views/home_view.dart';
import 'package:symbiot_flutter/views/keys_view.dart';
import 'package:symbiot_flutter/views/settings_view.dart';
import 'package:symbiot_flutter/widgets/symbiot_navigation_bar.dart';
import 'package:symbiot_flutter/widgets/symbiot_scaffold.dart';

import 'controllers/key_controller.dart';
import 'controllers/operation_controller.dart';

class SymbiotApp extends StatefulWidget {
  final List<ChangeNotifierProvider> providers;

  SymbiotApp({super.key}): providers = [
    ChangeNotifierProvider<KeyController>.value(
      value: KeyController.getInstance(),
    ),
    ChangeNotifierProvider<OperationController>.value(
        value: OperationController.getInstance(),
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

            const SizedBox(height: 20),

            // TODO: remove on prod
            const ApiControlPanelButton(),

            _body(selected),
          ],
        ),
      ),
    );
  }
}