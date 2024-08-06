import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')
    print(SECRET_KEY )
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///instance/database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

