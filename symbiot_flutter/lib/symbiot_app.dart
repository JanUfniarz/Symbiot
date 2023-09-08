import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/views/home_view.dart';
import 'package:symbiot_flutter/views/keys_view.dart';
import 'package:symbiot_flutter/views/settings_view.dart';
import 'package:symbiot_flutter/widgets/symbiot_navigation_bar.dart';
import 'package:symbiot_flutter/widgets/symbiot_scaffold.dart';

import 'BLoCs/key_manager_bloc.dart';

class SymbiotApp extends StatefulWidget {
  final KeyManager keyManager;

  const SymbiotApp({super.key,
    required this.keyManager
  });

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
        providers: [
          ChangeNotifierProvider<KeyManager>.value(
              value: widget.keyManager
          ),
        ],
        child: MaterialApp(
            home: SymbiotScaffold(
              tittle: SymbiotNavigationBar.labels[selected],
              body: Column(
                children: <Widget>[

                  SymbiotNavigationBar(
                    selected: selected,
                    onSelect: (index) => setState(
                            () => selected = index),
                  ),

                  _body(selected),

                ],
              ),
            ),
        ));
  }
}