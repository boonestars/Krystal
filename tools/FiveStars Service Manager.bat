START "" c:\Fivestars\FSSM\tools\rktools\rktools.msi /qn /norestart /l* C:\fivestars\FSSM\tools\rktools_log.txt

IF NOT EXIST "C:\Program Files (x86)" GOTO PROGRAMFILES
"C:\Program Files (x86)\Windows Resource Kits\Tools\Instsrv.exe" "FiveStars Service Manager" "C:\Program Files (x86)\Windows Resource Kits\Tools\Srvany.exe"
:PROGRAMFILES
"C:\Program Files\Windows Resource Kits\Tools\Instsrv.exe" "FiveStars Service Manager" "C:\Program Files\Windows Resource Kits\Tools\Srvany.exe"

regedit.exe /s "c:\FiveStars\FSSM\tools\win7service_fix.reg"

net start "FiveStars Service Manager"