import 'package:flutter/material.dart';
import 'package:symbiot_flutter/first_connector.dart';

class ApiControlPanel extends StatefulWidget {
  const ApiControlPanel({
    super.key,
    required this.connector
  });

  final FirstConnector connector;

  @override
  State<ApiControlPanel> createState() => _ApiControlPanelState();
}

class _ApiControlPanelState extends State<ApiControlPanel> {

  String message = "";

  String argument = "";


  // ====== Metody ======
  void _redirectMethod(int index) {
    switch (index) {

      case 0:
        widget.connector
            .readData()
            .then((value) => setState(
            () => message = value["message"]
        ));
        break;

      case 1:
        widget.connector
            .updateData();
            //TODO .then((value) => null),
        break;

      case 2:
        widget.connector.createData();
        //TODO .then((value) => null),
        break;

      case 3:
        //TODO widget.connector.deleteData(id);
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