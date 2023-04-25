#include "flutter_window.h"

#include <optional>

#include "flutter/generated_plugin_registrant.h"

// To MethodChannel
#include <flutter/binary_messenger.h>
#include <flutter/standard_method_codec.h>
#include <flutter/method_channel.h>
#include <flutter/method_result_functions.h>

// To map conversion
#include <any>
#include <map>
#include <string>
#include <flutter/flutter_view.h>

// To python
#include <Python.h>

FlutterWindow::FlutterWindow(const flutter::DartProject& project)
    : project_(project) {}

FlutterWindow::~FlutterWindow() {}


// ===========================================
// call.arguments -> map conversion
std::map<std::string, std::any> methodCallToMap(const flutter::MethodCall<flutter::EncodableValue>& call) {
    std::map<std::string, std::any> result;
    auto arguments = call.arguments();
    if (std::holds_alternative<flutter::EncodableMap>(*arguments)) {
        flutter::EncodableMap map = std::get<flutter::EncodableMap>(*arguments);
        // Iterate over the key-value pairs of the map
        for (const auto& pair : map) {
            const std::string& key = std::get<std::string>(pair.first);
            const flutter::EncodableValue& value = pair.second;
            // Convert the value to an any object and insert it into the result map
            if (std::holds_alternative<std::string>(value)) {
                result[key] = std::get<std::string>(value);
            } else if (std::holds_alternative<int>(value)) {
                result[key] = std::get<int>(value);
            } else if (std::holds_alternative<double>(value)) {
                result[key] = std::get<double>(value);
            } else if (std::holds_alternative<bool>(value)) {
                result[key] = std::get<bool>(value);
            } else {
                // Unsupported argument type
                result[key] = std::any();
            }
        }
    }
    return result;
}
// ===========================================

std::string pyObjectToString(PyObject* obj) {
    // Check if the object is a Unicode string
    if (PyUnicode_Check(obj)) {
        // Convert the Unicode string to a UTF-8 encoded C string
        const char* utf8Str = PyUnicode_AsUTF8(obj);
        if (utf8Str != nullptr) {
            return std::string(utf8Str);
        }
    }
    // If the object is not a Unicode string, get its string representation
    PyObject* strObj = PyObject_Str(obj);
    if (strObj == nullptr) {
        return "";
    }
    // Convert the string representation to a UTF-8 encoded C string
    const char* utf8Str = PyUnicode_AsUTF8(strObj);
    if (utf8Str == nullptr) {
        Py_DECREF(strObj);
        return "";
    }
    std::string result = std::string(utf8Str);
    Py_DECREF(strObj);
    return result;
}

// ===========================================
// MethodCannel
void initMethodChannel(flutter::FlutterEngine* flutter_instance, PyObject* connector) {
    // name your channel
    const static std::string channel_name("com.flutter.main/Channel");

    auto channel =
        std::make_unique<flutter::MethodChannel<>>(
            flutter_instance->messenger(), channel_name,
            &flutter::StandardMethodCodec::GetInstance());

    channel->SetMethodCallHandler(
        [connector](const flutter::MethodCall<>& call,
            std::unique_ptr<flutter::MethodResult<>> result) {

                std::map<std::string, std::any> arguments = methodCallToMap(call);

                // cheack method name called from dart
                if (call.method_name().compare("respond") == 0) {
                    // do whate ever you want

                    std::string prompt = std::any_cast<std::string>(arguments.at("prompt"));

                    if (connector) {
                        PyObject* my_function = PyObject_GetAttrString(connector, "respond");

                        if (my_function && PyCallable_Check(my_function)) {
                            PyObject* args = PyUnicode_FromString(prompt.c_str());// Przygotowanie argumentów funkcji
                            PyObject* resFromPy = PyObject_CallObject(my_function, args); // Wywołanie funkcji

                            // Sprawdzenie wyniku i przetworzenie go w zależności od oczekiwanego typu
                            if (resFromPy) {
                                // Przetworzenie wyniku np. jako int, float, string, itp.
                                // ...

                                std::string resToDart = pyObjectToString(resFromPy);
                                result->Success(resToDart);
                                Py_DECREF(resFromPy); // Zwolnienie obiektu wyniku
                            }
                            else {
                                // Obsługa błędu
                                // ...
                                result->Error("function error");
                            }

                            Py_DECREF(my_function); // Zwolnienie obiektu funkcji
                            Py_DECREF(args); // Zwolnienie obiektu argumentów
                        }
                        
                    } else {

                        // Obsługa błędu
                        // ...
                        result->Error("connector error");
                    }
                }else {
                    result->NotImplemented();
                }
        }
  );
}
// ===========================================

bool FlutterWindow::OnCreate() {
  if (!Win32Window::OnCreate()) {
    return false;
  }

  // Inicjalizacja interpretera Pythona
  Py_Initialize();

  // Zaimportowanie modułu Pythona
  PyObject* connector = PyImport_ImportModule("android/app/src/main/python/Connector.py");

  RECT frame = GetClientArea();

  // The size here must match the window dimensions to avoid unnecessary surface
  // creation / destruction in the startup path.
  flutter_controller_ = std::make_unique<flutter::FlutterViewController>(
      frame.right - frame.left, frame.bottom - frame.top, project_);
  // Ensure that basic setup of the controller was successful.
  if (!flutter_controller_->engine() || !flutter_controller_->view()) {
    return false;
  }
  RegisterPlugins(flutter_controller_->engine());
  // ===========================================
  // initialize method channel here 
  initMethodChannel(flutter_controller_->engine(), connector);

  //?run_loop_->RegisterFlutterInstance(flutter_controller_->engine());
  // ===========================================
  SetChildContent(flutter_controller_->view()->GetNativeWindow());

  flutter_controller_->engine()->SetNextFrameCallback([&]() {
    this->Show();
  });

  return true;
}

void FlutterWindow::OnDestroy() {
  if (flutter_controller_) {
    flutter_controller_ = nullptr;
  }

  Win32Window::OnDestroy();
}

LRESULT
FlutterWindow::MessageHandler(HWND hwnd, UINT const message,
                              WPARAM const wparam,
                              LPARAM const lparam) noexcept {
  // Give Flutter, including plugins, an opportunity to handle window messages.
  if (flutter_controller_) {
    std::optional<LRESULT> result =
        flutter_controller_->HandleTopLevelWindowProc(hwnd, message, wparam,
                                                      lparam);
    if (result) {
      return *result;
    }
  }

  switch (message) {
    case WM_FONTCHANGE:
      flutter_controller_->engine()->ReloadSystemFonts();
      break;
  }

    // Zakończenie interpretera Pythona
    Py_Finalize();

  return Win32Window::MessageHandler(hwnd, message, wparam, lparam);
}
