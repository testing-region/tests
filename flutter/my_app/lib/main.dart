// import flutter package to use flutter sdk in dart
import 'package:flutter/material.dart';

// main() is the function that the dart compiler looks for
// when a dart file is run. It is more like the main() 
// function in C/C++
void main() {
// To see the app, we need to call the runApp() function
// It takes a widget object as an argument
    runApp(MyApp());
}

// To create the app, we need to make a widget. In flutter,
// Everything is a widget. The StatelessWidget gives our app 
// the properities of a widget
class MyApp extends StatelessWidget {

// Widget is a custom data type that is used to refer that  
// an object takes the value of a widget.

// Seems a default build() function is needed
// It is used to build context, though I don't get the logic 
// behind it yet. The naming makes so much sense. Nice one GOOGLE
    Widget build(BuildContext context) {

    // Since we want our app to use material ui convention, we 
    // return the MaterialApp class. It takes named arguments.
	return MaterialApp(home: Text("Hello World!"),);
    }
}
