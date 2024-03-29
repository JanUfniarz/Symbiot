// ignore_for_file: avoid_print, curly_braces_in_flow_control_structures

import 'package:flutter/material.dart';
import 'package:symbiot_flutter/models/operation_model.dart';

import '../components/command_executor.dart';
import '../components/connection/operation_connector.dart';
import '../ui/widgets/bordered_button.dart';

class ApiControlPanelButton extends StatelessWidget {
  const ApiControlPanelButton({super.key});

  @override
  Widget build(BuildContext context) {
    return BorderedButton(
      onTap: () => Navigator.of(context).push(
          MaterialPageRoute(
              builder: (context) => ApiControlPanel(
                  connector: OperationConnector()
              )
          )
      ),
      icon: Icons.api_outlined,
      text: "Control\nPanel",
    );
  }
}


class ApiControlPanel extends StatefulWidget {
  const ApiControlPanel({
    super.key,
    required this.connector,
  });

  final OperationConnector connector;

  @override
  State<ApiControlPanel> createState() => _ApiControlPanelState();
}

class _ApiControlPanelState extends State<ApiControlPanel> {

  String message = "";

  String? argument;


  // ====== Metody ======
  void _redirectMethod(int index) async {
    switch (index) {

      case 0: /// GET
        await widget.connector
            .getAllOperations()
            .then((value) {
              OperationModel model = OperationModel(value[0]);
              print("=============");
              print(model.name);
              print(model.records[0].inputs[1]);
              print(model.records[1].previous.inputs[1]);
              print("=============");
            });

        break;

      case 1: /// PUT

        break;

      case 2: /// POST
        bool execute = false;
        await widget.connector
            .createOperation(argument ?? "")
            .then((value) => setState(
                () {
              // message = value["command"];
              // execute = value["execute"];
                  message = value["message"];
            }
        ));

        print(message);

        if (execute)
          CommandExecutor.powerShell()
              .run(message);

        break;

      case 3: /// DELETE
        print("del");
        // widget.connector.deleteOperation();
        //TODO .then((value) => null),
        break;
    }
  }


  final List<String> _requests = [
    "GET", "PUT",
    "POST", "DELETE",
  ];

  @override
  Widget build(BuildContext context) {

    // ====== Przyciski ======
    List<Widget> buttons = List.generate(
        _requests.length,
            (index) => Padding(
              padding: const EdgeInsets.all(20),
              child: SizedBox(
                height: 100,
                width: 150,
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.pink[900],
                  ),

                  onPressed: () => _redirectMethod(index),

                  child: Text(
                      _requests[index],
                  ),
                ),
              ),
            )
    );


    return Scaffold(
      backgroundColor: Colors.grey[900],
      appBar: AppBar(
        backgroundColor: Colors.pink[900],
        title: const Text("API Control Panel"),
        centerTitle: true,
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [

          Container(
            color: Colors.grey[350],
            width: 400,

            child: TextField(
              onChanged: (text) => argument = text,
            ),
          ),

          Padding(
            padding: const EdgeInsets.symmetric(vertical: 50),
            child: ClipRRect(
              borderRadius: const BorderRadius.all(Radius.circular(10)),
              child: Container(
                color: Colors.grey[350],
                child: Padding(
                  padding: const EdgeInsets.all(20.0),


                  child: Text(
                      "Message:\n$message",
                    style: const TextStyle(
                      fontSize: 26
                    ),
                    textAlign: TextAlign.center,
                  ),
                ),
              ),
            ),
          ),

          Divider(
            color: Colors.pink[900],
            thickness: 2,
          ),

          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: <Widget>[
              Column(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: <Widget>[buttons[0], buttons[1]],
              ),
              Column(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [buttons[2], buttons[3]],
              ),
            ],
          ),
        ],
      ),
    );
  }
}