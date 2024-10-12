import sys
import subprocess

# Install ReportLab using pip
try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pytesseract'])
    print("ReportLab installed successfully.")
except subprocess.CalledProcessError:
    print("Error occurred while installing ReportLab.")
