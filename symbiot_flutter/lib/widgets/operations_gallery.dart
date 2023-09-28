import 'package:flutter/material.dart';

import '../palette.dart';
import 'operation_card.dart';

class OperationsGallery extends StatelessWidget {
  const OperationsGallery({
    super.key,
    required this.primary,
    this.operationsCards,
  });

  final Color primary;
  final List<OperationCard>? operationsCards;

  @override
  Widget build(BuildContext context) => Padding(
    padding: const EdgeInsets.symmetric(horizontal: 80),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[

        const Padding(
          padding: EdgeInsets.symmetric(horizontal: 10),

          child: Text(
            "Operations",
            style: TextStyle(
              color: Palette.primary,
              fontSize: 24,
            ),
          ),
        ),

        Divider(
          color: primary,
          thickness: 2,
        ),

        SingleChildScrollView(
          child: Row(
            children: operationsCards ?? [],
          ),
        ),

        const SizedBox(height: 20),

      ],
    ),
  );
}