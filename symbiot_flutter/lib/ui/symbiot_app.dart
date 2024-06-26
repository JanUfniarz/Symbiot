import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/tests/api_control_panel.dart';
import 'package:symbiot_flutter/ui/style/palette.dart';
import 'package:symbiot_flutter/ui/views/home_view.dart';
import 'package:symbiot_flutter/ui/views/keys_view.dart';
import 'package:symbiot_flutter/ui/views/settings_view.dart';
import 'package:symbiot_flutter/ui/widgets/symbiot_navigation_bar.dart';
import 'package:symbiot_flutter/ui/widgets/symbiot_scaffold.dart';

class SymbiotApp extends StatefulWidget {
  final List<ChangeNotifierProvider> providers;

  const SymbiotApp({super.key, required this.providers});

  static Future<dynamic> push(BuildContext context, Widget view) =>
      Navigator.push(context, MaterialPageRoute(
          builder: (context) => view));

  static void back(BuildContext context, {result}) => Navigator.of(context).pop(result);

  static Future<dynamic> bottomSheet(
      BuildContext context,
      Widget? child,
      ) => showModalBottomSheet(
    context: context,
    isScrollControlled: true,
    backgroundColor: Palette.backgroundGrey,
    shape: const RoundedRectangleBorder(
      borderRadius: BorderRadius.only(
        topRight: Radius.circular(24),
        topLeft: Radius.circular(24),
      ),
    ),
    builder: (context) => Padding(
      padding: EdgeInsets.only(
          bottom: MediaQuery.of(context)
              .viewInsets.bottom
      ),
      child: SizedBox(
        height: 300,
        child: child,
      ),
    ),
  );

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
  Widget build(BuildContext context) => MultiProvider(
    providers: widget.providers,
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

            const SizedBox(height: 20),

            // TODO: remove on prod
            const ApiControlPanelButton(),

            _body(selected),
          ],
        ),
      )
    ),
  );
}