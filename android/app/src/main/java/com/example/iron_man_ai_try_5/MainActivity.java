package com.example.iron_man_ai_try_5;


import androidx.annotation.NonNull;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

import java.util.Map;

import io.flutter.embedding.android.FlutterActivity;
import io.flutter.embedding.engine.FlutterEngine;
import io.flutter.plugin.common.MethodChannel;

public class MainActivity extends FlutterActivity {

    private static final String CHANNEL = "com.flutter.main/Channel";

    @Override
    public void configureFlutterEngine(@NonNull FlutterEngine flutterEngine) {
        super.configureFlutterEngine(flutterEngine);

        if (!Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }

        PyObject connector = Python
                .getInstance()
                .getModule("Connector");

                

        new MethodChannel(flutterEngine.getDartExecutor().getBinaryMessenger(), CHANNEL)
                .setMethodCallHandler(
                        (call, result) -> {
                            final Map<String, Object> arguments = call.arguments();

                            switch (call.method) {

                                default:
                                    result.notImplemented();
                                    break;

                                case "respond":
                                    result.success(connector.callAttr(call.method,
                                            arguments.get("prompt")
                                    ).toString());
                                    break;

                            }
                        }
                );
    }
}
