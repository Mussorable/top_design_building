import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, request
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_babel import Babel

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

assets = Environment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if not app.debug and not app.testing:
    if app.config['LOG_TO_STDOUT']:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    else:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/manager.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('App startup')

babel = Babel(app, locale_selector=get_locale)

js_bundle = Bundle('js/main.js', filters='jsmin', output='js/main.min.js')
assets.register('js_all', js_bundle)

css_bundle = Bundle('css/main.scss', filters='libsass', output='css/main.min.css')
assets.register('css_all', css_bundle)

from app import routes, forms, models
