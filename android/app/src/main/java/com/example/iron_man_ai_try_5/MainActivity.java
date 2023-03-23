package com.example.iron_man_ai_try_5;


import androidx.annotation.NonNull;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

import java.util.Map;

import io.flutter.embedding.android.FlutterActivity;
import io.flutter.embedding.engine.FlutterEngine;
import io.flutter.plugin.common.MethodChannel;
import io.github.cdimascio.dotenv.Dotenv;

public class MainActivity extends FlutterActivity {

    private static final String CHANNEL = "com.flutter.main/Channel";

    @Override
    public void configureFlutterEngine(@NonNull FlutterEngine flutterEngine) {
        super.configureFlutterEngine(flutterEngine);

        if (!Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }

        Dotenv dotenv = Dotenv.configure().load();
        String apiKey =  dotenv.get("OPENAI_API_KEY");

        PyObject connector = Python
                .getInstance()
                .getModule("Connector");

        connector.callAttr("initialize", apiKey);

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

//* -----------------------------------------------
/*

public class WaitNotifyExample {
    public static void main(String[] args) {
        Message msg = new Message("process it");
        Waiter waiter = new Waiter(msg);
        new Thread(waiter,"waiter").start();

        Notifier notifier = new Notifier(msg);
        new Thread(notifier, "notifier").start();
        System.out.println("All the threads are started");
    }
}
class Message {
    private String msg;

    public Message(String str){
        this.msg=str;
    }

    public String getMsg() {
        return msg;
    }

    public void setMsg(String str) {
        this.msg=str;
    }
}

class Waiter implements Runnable{

    private Message msg;

    public Waiter(Message m){
        this.msg=m;
    }

    @Override
    public void run() {
        String name = Thread.currentThread().getName();
        synchronized (msg) {
            try{
                System.out.println(name+" waiting to get notified at time:"+System.currentTimeMillis());
                msg.wait();
            }catch(InterruptedException e){
                e.printStackTrace();
            }
            System.out.println(name+" waiter thread got notified at time:"+System.currentTimeMillis());
            //process the message now
            System.out.println(name+" processed: "+msg.getMsg());
        }
    }
}

class Notifier implements Runnable {

    private Message msg;

    public Notifier(Message msg) {
        this.msg = msg;
    }

    @Override
    public void run() {
        String name = Thread.currentThread().getName();
        System.out.println(name+" started");
        try {
            Thread.sleep(1000);
            synchronized (msg) {
                msg.setMsg(name+" Notifier work done");
                //msg.notify();
                msg.notifyAll();
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }
}
*/
