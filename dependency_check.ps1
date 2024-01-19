$ErrorActionPreference = "SilentlyContinue"

$good = "`e[34m[✓]`e[0m"
$bad = "`e[34m[✗]`e[0m"

if (Test-Path -Path (Get-Command flutter -ErrorAction SilentlyContinue).Source) {
    Write-Host "$good Flutter installed"
    flutter doctor | Select-String -SimpleMatch "Windows" | ForEach-Object {
        Write-Host "`e[34m$($_.Line.Substring(0, [Math]::Min(3, $_.Line.Length)))`e[0m$($_.Line.Substring(3))"
    }
} else { Write-Host "$bad Flutter not installed or not added to PATH" }

if (Test-Path -Path (Get-Command docker -ErrorAction SilentlyContinue).Source) {
    Write-Host "$good Docker installed"

    $info = @{
        "Client" = $null
        "Server" = $null
    }

    try { $info["Client"] = docker version --format '{{.Client.Version}}' } catch { }
    try { $info["Server"] = docker version --format '{{.Server.Version}}' } catch { }

    foreach ($key in $info.Keys) {
        if ($info[$key]) {
            Write-Host "$good Docker $key working. version: $($info[$key])"
        } else {
            Write-Host "$bad Docker $key not working"
        }
    }
} else { Write-Host "$bad Docker not installed or not added to PATH" }