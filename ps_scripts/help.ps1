Write-Host "
   Symbiot available options:
" -ForegroundColor Green
Write-Host "
    __________________________________________________________________
   | OPTION |     ARGUMENTS      |            DESCRIPTION             |
   |________|____________________|____________________________________|
" -ForegroundColor Blue -NoNewline
Write-Host "   | help   |                    | Shows this                         |
   |        |                    | information.                       |
   |________|____________________|____________________________________|
   | run    |                    | Starts the                         |
   |        |                    | Symbiot app.                       |
   |________|____________________|____________________________________|
   | src    |                    | Moves you to the                   |
   |        |                    | source directory.                  |
   |________|____________________|____________________________________|
   | clean  | lib, server, db,   | Deletes the image or build dir.    |
   |        | engine, flutter    | Without args it cleens everything. |
   |________|____________________|____________________________________|
   | build  | lib, server, db,   | Builds the image or build dir.     |
   |        | engine, flutter    | Without args it builds everything. |
   |________|____________________|____________________________________|
   | check  |                    | Checks the dependencies.           |
   |        |                    |                                    |
   |________|____________________|____________________________________|
"