import 'package:flutter/material.dart';

import '../palette.dart';

class NavigationElement extends StatelessWidget {
  final IconData icon;
  final String label;
  final bool selected;
  final void Function() onTap;

  const NavigationElement({super.key,
    required this.icon,
    required this.label,
    required this.selected,
    required this.onTap
  });

  @override
  Widget build(BuildContext context) {
    Color color = selected
        ? Palette. primary
        : Palette.accent;

    return InkWell(
      onTap: onTap,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(
            icon,
            color: color
          ),
          Text(
            label,
            style: TextStyle(
              color: color
            ),
          ),
        ],
      ),
    );
  }
}
