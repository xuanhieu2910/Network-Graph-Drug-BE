import os
from pathlib import Path
from dotenv import load_dotenv


# Load file .env
load_dotenv(dotenv_path=r'D:\Personal\Research\Network-Graph-Drug-BE\properties.env')

class Settings():
    DB_HOST = os.getenv("DB_HOST", "202.191.56.108")
    DB_PORT = int(os.getenv("DB_PORT", "3306"))
    DB_USER = os.getenv("DB_USER", "bind_db")
    DB_PASSWORD = os.getenv("DB_PASSWORD","Hoangyen061120@")
    DB_NAME = os.getenv("DB_NAME","bind")


settings = Settings()