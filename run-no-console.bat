set PYTHONDONTWRITEBYTECODE=1
cd env\Scripts
call activate.bat
cd ..\..
python compile_ui.py
cd src
start pythonw main.py