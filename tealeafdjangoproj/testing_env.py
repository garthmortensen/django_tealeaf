from pathlib import Path
import os
from dotenv import load_dotenv

# Determine the correct path for the .env file
# This assumes the .env file is in the same directory as the settings.py file
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR / '.env'
load_dotenv(dotenv_path)

SECRET_KEY = os.getenv("SECRET_KEY")

# Debug print statements (optional, remove in production)
print("SECRET_KEY:", SECRET_KEY)

# Detect if running on PythonAnywhere
if 'PYTHONANYWHERE_DOMAIN' in os.environ:
    print("PYTHONANYWHERE environment is detected")
else:
    print("PYTHONANYWHERE environment is not detected")
