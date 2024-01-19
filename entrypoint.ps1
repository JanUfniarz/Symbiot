Write-Host "Welcome to the Symbiot App!" -ForegroundColor Green

If (-not $(docker images symbiot_lib_builder -q)) {
    Write-Host "Building symbiot_lib ..." -ForegroundColor Yellow
    Set-Location symbiot_lib
    docker build -t symbiot_lib_builder .
    Set-Location ..
}

Write-Host "Building symbiot_server and symbiot_core ..." -ForegroundColor Yellow
docker-compose up --detach
Set-Location symbiot_flutter

Write-Host "
 ________        ___    ___  _____ ______       ________      ___      ________      _________
|\   ____\      |\  \  /  /||\   _ \  _   \    |\   __  \    |\  \    |\   __  \    |\___   ___\
\ \  \___|_     \ \  \/  / /\ \  \\\__\ \  \   \ \  \|\ /_   \ \  \   \ \  \|\  \   \|___ \  \_|
 \ \_____  \     \ \    / /  \ \  \\|__| \  \   \ \   __  \   \ \  \   \ \  \\\  \       \ \  \
  \|____|\  \     \/  /  /    \ \  \    \ \  \   \ \  \|\  \   \ \  \   \ \  \\\  \       \ \  \
    ____\_\  \  __/  / /       \ \__\    \ \__\   \ \_______\   \ \__\   \ \_______\       \ \__\
   |\_________\|\___/ /         \|__|     \|__|    \|_______|    \|__|    \|_______|        \|__|
   \|_________|\|___|/
" -ForegroundColor Green

if (-not $(Test-Path keys.txt -PathType Leaf)) {
    New-Item -Path keys.txt -ItemType File
}

Write-Host "Building symbiot_flutter ..." -ForegroundColor Yellow
flutter run
Set-Location ..
docker-compose down

Write-Host "Symbiot App closed" -ForegroundColor Green