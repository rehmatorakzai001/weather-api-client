import os
from dotenv import load_dotenv

load_dotenv()

def weather_api_key():
    return os.getenv("API_KEY")