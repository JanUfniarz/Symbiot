import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:symbiot_flutter/controllers/operation_controller.dart';

import '../widgets/symbiot_scaffold.dart';

class OperationView extends StatelessWidget {
  const OperationView({super.key});

  @override
  Widget build(BuildContext context) => Consumer<OperationController>(
    builder: (context, controller, child) => SymbiotScaffold(
      tittle: controller.model!.name,
    ),
  );
}