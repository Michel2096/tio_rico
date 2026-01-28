import os
from dotenv import load_dotenv

class Config:
    Env = os.getenv('FLASK_ENV_')