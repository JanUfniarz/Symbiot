import 'package:flutter/material.dart';
import 'package:symbiot_flutter/tests/api_control_panel.dart';
import 'package:symbiot_flutter/ui/views/home_view.dart';
import 'package:symbiot_flutter/ui/views/keys_view.dart';
import 'package:symbiot_flutter/ui/views/settings_view.dart';
import 'package:symbiot_flutter/ui/widgets/symbiot_navigation_bar.dart';
import 'package:symbiot_flutter/ui/widgets/symbiot_scaffold.dart';

class SymbiotApp extends StatefulWidget {
  const SymbiotApp({super.key});

  static Future<dynamic> push(BuildContext context, Widget view) =>
      Navigator.push(context, MaterialPageRoute(
          builder: (context) => view));

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
    return SymbiotScaffold(
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
    );
  }
}