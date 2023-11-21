import 'package:flutter/material.dart';

import '../style/palette.dart';

class OperationCard extends StatelessWidget {
  const OperationCard({
    super.key,
    required this.name,
    required this.onTap,
  });

  final Color primaryColor = Palette.primary;

  final String name;

  final void Function() onTap;

  @override
  Widget build(BuildContext context) => InkWell(
        onTap: onTap,
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
