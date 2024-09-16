import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    TITLE = 'Top Design'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ASSETS_DEBUG = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    CONTACT_EMAIL = 'redduck5601@gmail.com'
    CONTACT_PHONE = '+48123456789'
    ADMINS = os.environ.get('MAIL_SENDER')
    LANGUAGES = ['pl', 'en', 'de']
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
