#include "flutter_window.h"

#include <optional>

#include "flutter/generated_plugin_registrant.h"

#include <flutter/binary_messenger.h>
#include <flutter/standard_method_codec.h>
#include <flutter/method_channel.h>
#include <flutter/method_result_functions.h>

#include <any>
#include <map>
#include <string>
#include <flutter/flutter_view.h>

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

// ===========================================
// MethodCannel
void initMethodChannel(flutter::FlutterEngine* flutter_instance) {
    // name your channel
    const static std::string channel_name("com.flutter.main/Channel");

    auto channel =
        std::make_unique<flutter::MethodChannel<>>(
            flutter_instance->messenger(), channel_name,
            &flutter::StandardMethodCodec::GetInstance());

    channel->SetMethodCallHandler(
        [](const flutter::MethodCall<>& call, 
          std::unique_ptr<flutter::MethodResult<>> result) {

            std::map<std::string, std::any> arguments = methodCallToMap(call);

            // cheack method name called from dart
            if (call.method_name().compare("respond") == 0) {
            // do whate ever you want

            std::string res = std::any_cast<std::string>(arguments.at("prompt"));

            result->Success(res);
            }
            else {
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
    initMethodChannel(flutter_controller_->engine());

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

  return Win32Window::MessageHandler(hwnd, message, wparam, lparam);
}
