import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hardcodedsecret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

