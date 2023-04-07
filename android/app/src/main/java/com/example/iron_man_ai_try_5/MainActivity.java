package com.example.iron_man_ai_try_5;


import androidx.annotation.NonNull;

// For quaquopy
import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

import java.util.Map;

// For flutter and MethodChannel
import io.flutter.embedding.android.FlutterActivity;
import io.flutter.embedding.engine.FlutterEngine;
import io.flutter.plugin.common.MethodChannel;

public class MainActivity extends FlutterActivity {

    // MethodChannel ID
    private static final String CHANNEL = "com.flutter.main/Channel";

    // Method on start of app
    @Override
    public void configureFlutterEngine(@NonNull FlutterEngine flutterEngine) {
        super.configureFlutterEngine(flutterEngine);

        // Python start
        if (!Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }

        // Declaration of connector file
        PyObject connector = Python
                .getInstance()
                .getModule("Connector");

        // MethodChannel
        new MethodChannel(flutterEngine.getDartExecutor().getBinaryMessenger(), CHANNEL)
                .setMethodCallHandler(
                        // Function on call to channel
                        (call, result) -> {
                            // Declaration of arguments map
                            final Map<String, Object> arguments = call.arguments();

                            // All methods called by it's name
                            switch (call.method) {

                                // Case if method name is not supported
                                default:
                                    result.notImplemented();
                                    break;

                                // Method called by writing prompt and send button press
                                case "respond":
                                    result.success(                         // Return to dart
                                            connector.callAttr(             // Result of method in Connector
                                                    call.method,            // Name of method
                                                    arguments.get("prompt") // Prompt taken from arguments map
                                            ).toString());                  // In form of string
                                    break;

                                // Method to set an API key
                                case "setApiKey":
                                    result.success(                          // Return to dart
                                            connector.callAttr(              // Result of method in Connector
                                                    call.method,             // Name of method
                                                    arguments.get("API_KEY") // Api key taken from arguments map
                                            ));                              // Without any return value
                                    break;
                            }
                        }
                );
    }
}