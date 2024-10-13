param([string[]]$params)

Set-Location ..
$all =  $params.Count -eq 0

if ($params -contains "lib" -or $all) { docker rmi symbiot_lib_builder }

if ($params -contains "engine" -or $all) {
    docker stop symbiot-engine-1
    docker rm symbiot-engine-1
    docker rmi symbiot-engine
}

if ($params -contains "server" -or $all) {
    docker stop symbiot-server-1
    docker rm symbiot-server-1
    docker rmi symbiot-server
}

if ($params -contains "db" -or $all) {
    docker stop symbiot-database-1
    docker rm symbiot-database-1
    docker rmi postgres
}

if ($params -contains "flutter" -or $all) {
    Set-Location symbiot_flutter
    flutter clean
}