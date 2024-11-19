@echo off
:: Crea el entorno virtual si no existe
if not exist "venv" (
    python -m venv venv
)

:: Activa el entorno virtual
call venv\Scripts\activate.bat

:: Instala los paquetes de requirements.txt
pip install -r requirements.txt

:: Deja el terminal abierto
cmd /K
