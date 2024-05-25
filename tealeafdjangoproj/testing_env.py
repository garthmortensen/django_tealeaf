from pathlib import Path
import os
from dotenv import load_dotenv

home = Path.home() / ".env"
load_dotenv(home)
SECRET_KEY = os.getenv("SECRET_KEY")
print(SECRET_KEY)
