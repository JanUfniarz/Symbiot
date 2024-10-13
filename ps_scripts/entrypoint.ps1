Set-Location ..

Write-Host "Welcome to the Symbiot App!" -ForegroundColor Green
Write-Host "To check your dependencies run dependency_check.ps1 script" -BackgroundColor Blue

function CheckAndClose {
    docker-compose down
    Write-Host "Checking dependencies ..." -ForegroundColor Yellow
    & ./ps_scripts/dependency_check.ps1
    exit 1
}

if (-not $(docker images symbiot_lib_builder -q)) {
    Write-Host "Building symbiot_lib ..." -ForegroundColor Yellow
    Set-Location symbiot_lib
    docker build -t symbiot_lib_builder .
    Set-Location ..
}

Write-Host "Building symbiot_server and symbiot_engine ..." -ForegroundColor Yellow
docker-compose up --detach

$not_working_containers = New-Object System.Collections.ArrayList
foreach ($name in @("symbiot-server-1", "symbiot-database-1", "symbiot-engine-1")) {
    $null = $not_working_containers.Add($name)
}

docker container ls --format "{{.Names}}" | ForEach-Object {
    if ($not_working_containers.Contains($_)) { $not_working_containers.Remove($_) }
}
if ($not_working_containers.Count -gt 0) {
    foreach ($container in $not_working_containers) {
        Write-Host "Container $container did not build" -ForegroundColor Red
    }
    CheckAndClose
}

Write-Host "
 ________        ___    ___  _____ ______      ________     ___     ________     __________
|\   ____\      |\  \  /  /||\   _ \  _   \   |\   __  \   |\  \   |\   __  \   |\___   ___\
\ \  \___|_     \ \  \/  / /\ \  \\\__\ \  \  \ \  \|\ /_  \ \  \  \ \  \|\  \  \|___ \  \_|
 \ \_____  \     \ \    / /  \ \  \\|__| \  \  \ \   __  \  \ \  \  \ \  \\\  \      \ \  \
  \|____|\  \     \/  /  /    \ \  \    \ \  \  \ \  \|\  \  \ \  \  \ \  \\\  \      \ \  \
    ____\_\  \  __/  / /       \ \__\    \ \__\  \ \_______\  \ \__\  \ \_______\      \ \__\
   |\_________\|\___/ /         \|__|     \|__|   \|_______|   \|__|   \|_______|       \|__|
   \|_________|\|___|/
" -ForegroundColor Green

Set-Location symbiot_flutter

if (-not $(Test-Path keys.txt -PathType Leaf)) {
    New-Item -Path keys.txt -ItemType File
}

Write-Host "Building symbiot_flutter ..." -ForegroundColor Yellow

function RunFrontend {
    param ([int]$status = 0)

    flutter run 2>&1 | ForEach-Object {
        Write-Host $_ -ForegroundColor $(if (($_ -like "*Error*") -or ($_ -like "*Exception*")) {
            "Red"
        } elseif ($_ -like "*✓*") {
            "Green"
        } elseif ($_ -like "*...*") {
            "Yellow"
        } else {
            "White"
        })

        if ($_ -match "Exception: Build process failed") {
            if ($status -eq 0) {
                Write-Host "Cleaning and rebuilding ..." -BackgroundColor Blue
                flutter clean
                RunFrontend -status 1
            } elseif ($status -eq 1) {
                Set-Location ..
                CheckAndClose
            }
        }
    }
}
RunFrontend

Set-Location ..

docker-compose down
Write-Host "Symbiot App closed" -ForegroundColor Green
exit 0