import 'package:flutter/material.dart';
import 'package:symbiot_flutter/widgets/navigation_element.dart';

import '../palette.dart';

class SymbiotNavigationBar extends StatelessWidget {
  final int selected;
  final void Function(int) onSelect;

  const SymbiotNavigationBar({super.key,
    required this.selected,
    required this.onSelect,
  });

  static const List<IconData> _icons = [
    Icons.home_outlined,
    Icons.vpn_key_outlined,
    Icons.settings_outlined
  ];

  static const List<String> labels = [
    "Home", "Keys", "Settings"
  ];

  @override
  Widget build(BuildContext context) {
    return NavigationBar(
      height: 50,
      backgroundColor: Palette.background,
      shadowColor: Palette.primary,
      elevation: 5,
      destinations: List.generate(_icons.length,
              (index) => NavigationElement(
                icon: _icons[index],
                label: labels[index],
                selected: selected == index,
                onTap: () => onSelect(index),
              )
      ),
    );
    // return Container(
    //   height: 50,
    //   color: Palette.primary,
    //  
    //   child: Row(
    //   ),
    // );
  }
}