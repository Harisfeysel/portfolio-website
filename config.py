import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask-Mail settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')
    
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here') 