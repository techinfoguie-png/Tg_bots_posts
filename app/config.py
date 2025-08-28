# config.py
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')
TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
ML_MODEL_ENDPOINT = os.getenv('ML_MODEL_ENDPOINT')
CONTENT_GENERATOR_API = os.getenv('CONTENT_GENERATOR_API')
