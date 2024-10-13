param([string[]]$params)

Set-Location ..
$all =  $params.Count -eq 0

if ($params -contains "lib" -or $all) {
    Set-Location symbiot_lib
    docker build -t symbiot_lib_builder .
    Set-Location ..
}

if ($params -contains "engine" -or $all) {
    Set-Location symbiot_engine
    docker build -t symbiot-engine .
    Set-Location ..
}

if ($params -contains "server" -or $all) {
    Set-Location symbiot_server
    docker build -t symbiot-server .
    Set-Location ..
}

if ($params -contains "flutter" -or $all) {
    Set-Location symbiot_flutter
    flutter build windows
}