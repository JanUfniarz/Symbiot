Write-Host "Welcome to the Symbiot App!" -ForegroundColor Green

if (-not $(docker images symbiot_lib_builder -q)) {
    Write-Host "Building symbiot_lib ..." -ForegroundColor Yellow
    Set-Location symbiot_lib
    docker build -t symbiot_lib_builder .
    Set-Location ..
}

Write-Host "Building symbiot_server and symbiot_core ..." -ForegroundColor Yellow
docker-compose up --detach

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

flutter run 2>&1 | ForEach-Object {
    Write-Host $_ -ForegroundColor $(if (($_ -like "*Error*") -or (($_ -like "*Exception*"))) {
        "Red"
    } elseif ($_ -like "*✓*") {
        "Green"
    } elseif ($_ -like "*...*") {
        "Yellow"
    } else {
        "White"
    })

    if ($_ -match "Exception: Build process failed") {
        Write-Host "Cleaning and rebuilding ..." -ForegroundColor Yellow
        flutter clean
        flutter run
    }
}
Set-Location ..

docker-compose down
Write-Host "Symbiot App closed" -ForegroundColor Green