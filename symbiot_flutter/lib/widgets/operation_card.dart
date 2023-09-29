import 'package:flutter/material.dart';

import '../palette.dart';
import '../views/operation_view.dart';

class OperationCard extends StatelessWidget {
  const OperationCard({
    super.key,
    required this.name,
    required this.before,
    required this.after,
  });
  final Color primaryColor = Palette.primary;

  final String name;

  final void Function()? before;
  final void Function()? after;

  @override
  Widget build(BuildContext context) => InkWell(

      onTap: () async {
        if (before == null) return;
        before!();
        await Navigator.push(
            context,
            MaterialPageRoute(
                builder: (context) => const OperationView()
            )
        );
        after!();
      },

      child: SizedBox(
        height: 128,
        width: 100,
        child: Card(
          color: primaryColor,
          child: Card(
            color: Palette.background,

            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [

                FittedBox(
                  fit: BoxFit.scaleDown,
                  child: Text(
                    name,
                    style: TextStyle(
                      color: primaryColor,
                      fontSize: 20,
                    ),
                  ),
                ),

                Icon(
                  Icons.star_half_rounded,
                  size: 60,
                  color: primaryColor,
                ),

              ],
            ),
          ),
        ),
      ),
    );
}