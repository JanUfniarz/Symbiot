# add this to the $Profile

# Symbiot cli
function symbiot {
    param([string]$command, [string[]]$params)
    $originalPath = $PWD.Path
    Set-Location $PSScriptRoot

    switch ($command) {
        help {& ./help.ps1}
        run {& ./entrypoint.ps1}
        src { Set-Location .. }
        clean {& ./clean.ps1 $params}
        build {& ./build.ps1 $params}
        check {& ./dependency_check.ps1 }
        default {Write-Host "To see available options run 'symbiot help'"}
    }
    if ($command -ne "src") { Set-Location $originalPath }
}
