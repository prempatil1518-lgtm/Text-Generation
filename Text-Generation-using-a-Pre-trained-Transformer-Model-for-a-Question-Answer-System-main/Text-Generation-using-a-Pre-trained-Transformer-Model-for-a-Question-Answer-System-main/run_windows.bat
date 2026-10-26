@echo off
echo Starting AI Question-Answer System...
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)
call venv\Scripts\activate
echo Installing/updating dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.
echo Launching application...
python app.py
pause
