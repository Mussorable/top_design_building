import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    TITLE = 'Perfect Space'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ASSETS_DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    CONTACT_EMAIL = 'contact@perfect-space.pl'
    CONTACT_PHONE = '+48723569435'
    ADMINS = os.environ.get('MAIL_SENDER')
    LANGUAGES = ['pl', 'en', 'de']
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
