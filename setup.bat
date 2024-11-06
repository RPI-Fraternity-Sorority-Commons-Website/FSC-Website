@echo off

set venvpath=.venv
set django__ver=5.1.1

echo Setting up FSC Website project (Django %django__ver%)...
echo Creating virtual environment: %venvpath%/
py -3 -m venv %venvpath% >nul
echo Installing Django %django__ver% in %venvpath%/
call .venv/scripts/activate >nul
py -m pip install --upgrade pip
py -m pip install Django==5.1.1
py -m pip install Pillow
%venvpath%\Scripts\python.exe manage.py migrate
%venvpath%\Scripts\python.exe manage.py project_init
echo Done
echo: