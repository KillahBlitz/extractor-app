@echo off
REM Script para configurar el entorno de desarrollo
REM Establece src como directorio principal de Python

set PROJECT_ROOT=%~dp0
set SRC_PATH=%PROJECT_ROOT%src

REM Agregar src al PYTHONPATH
set PYTHONPATH=%SRC_PATH%;%PYTHONPATH%

echo Configuracion del proyecto:
echo PROJECT_ROOT: %PROJECT_ROOT%
echo SRC_PATH: %SRC_PATH%
echo PYTHONPATH configurado con src como directorio principal

REM Activar entorno virtual si existe
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
    echo Entorno virtual activado
)

cmd /k