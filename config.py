import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ASSETS_DEBUG = True
