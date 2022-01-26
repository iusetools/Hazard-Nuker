python -m pip install -r requirements.txt
cls
echo python hazard.py >> start.bat
start start.bat
start /b "" cmd /c del "%~f0"&exit /b