$ErrorActionPreference = "SilentlyContinue"

$good = "`e[32m[✓]`e[0m"
$bad = "`e[31m[✗]`e[0m"

if (Test-Path -Path (Get-Command flutter -ErrorAction SilentlyContinue).Source) {
    Write-Host "$good Flutter installed"
    flutter doctor | Select-String -SimpleMatch "Windows" | ForEach-Object {
        $sign = $_.Line.Substring(0, [Math]::Min(3, $_.Line.Length))
        $sign = if ($sign -like "*✓*") {
            $good
        } elseif ($sign -like "*✗*") {
            $bad
        } else {
            "`e[33m$sign`e[0m"
        }
        Write-Host "$sign$($_.Line.Substring(3))"
    }
} else { Write-Host "$bad Flutter not installed or not added to PATH" }

if (Test-Path -Path (Get-Command docker -ErrorAction SilentlyContinue).Source) {
    Write-Host "$good Docker installed"

    $client = try { docker version --format '{{.Client.Version}}' } catch { $null }
    $server = try { docker version --format '{{.Server.Version}}' } catch { $null }

    if ($client) {
        Write-Host "$good Docker Client working. version: $client"
    } else {
        Write-Host "$bad Docker Client not working`n`t probably some instalation error"
    }
    if ($server) {
        Write-Host "$good Docker Server working. version: $server"
    } else {
        Write-Host "$bad Docker Server not working`n`t try to run docker desktop app"
    }
} else { Write-Host "$bad Docker not installed or not added to PATH" }