import 'package:flutter/material.dart';
import 'package:symbiot_flutter/first_connector.dart';
import 'package:symbiot_flutter/home_view.dart';

import 'api_control_panel.dart';

// void main() {
//
//   runApp(MaterialApp(
//     home: HomeView(
//       connector: FirstConnector(),
//     ),
//   ));
// }

void main() => runApp(MaterialApp(
  home: ApiControlPanel(
    connector: FirstConnector(),
  ),
));