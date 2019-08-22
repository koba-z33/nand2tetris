Write-Output "make venv"

python -m venv venv

Write-Output "activate venv"
.\venv\Scripts\Activate.ps1

Write-Output "pip upgrade"
python -m pip install --upgrade pip

Write-Output "pip install -r requirements.txt"
pip install -r requirements.txt