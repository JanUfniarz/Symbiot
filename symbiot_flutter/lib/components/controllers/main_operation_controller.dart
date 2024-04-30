import 'package:flutter/material.dart';
import 'package:symbiot_flutter/components/internal_cache.dart';

import '../../models/operation_model.dart';
import '../../models/record_model.dart';
import '../../ui/symbiot_app.dart';
import '../../ui/views/chat_view.dart';
import '../../ui/views/operation_view.dart';
import '../../ui/widgets/message_change_field.dart';
import '../connection/chat_connector.dart';
import '../connection/operation_connector.dart';
import 'operation_controller.dart';

class MainOperationController extends OperationController {
  MainOperationController(
      OperationConnector operationConnector,
      InternalCache cache
      ): super(operationConnector, cache) {
    loadData();
  }

  void openOperation(String id, BuildContext context) => SymbiotApp.push(
        context, OperationView(id)
    ).whenComplete(() => loadData());

  void openChat(RecordModel step, BuildContext context) =>
      SymbiotApp.push(context, ChatView(step.id));
  /*
  void openChat(RecordModel step, BuildContext context) =>
      _chatConnector.manageChat("open", step: step)
          .whenComplete(() => SymbiotApp.push(context, ChatView(step.id))
            .whenComplete(() => _chatConnector.manageChat("close")));
   */

  Future<OperationModel> newOperation(String wish) async {
    await operationConnector.createOperation(wish)
        .whenComplete(() => loadData());
    return cache.newOperations[0];
  }

  Future<void> deleteOperation(String id, BuildContext context) async =>
      operationConnector.deleteOperation(id)
          .then((_) => SymbiotApp.back(context))
          .whenComplete(() => loadData());

  Future<void> changeOperationName(String id, String newName) async {
    trigger();
    operationConnector.changeName(id, newName)
        .whenComplete(() => loadData());
  }
}