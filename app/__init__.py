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

assets = Environment()
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
babel = Babel()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    def get_locale():
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    assets.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    babel.init_app(app, locale_selector=get_locale)

    from app.cli import bp as cli_bp
    app.register_blueprint(cli_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        @app.context_processor
        def utility_processor():
            from app.main.forms import EmailForm
            email_form = EmailForm()

            return dict(email_form=email_form)

        @app.before_request
        def before_request():
            from flask import g
            g.locale = str(get_locale())

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

    js_bundle = Bundle('js/main.js', filters='jsmin', output='js/main.min.js')
    assets.register('js_all', js_bundle)

    css_bundle = Bundle('css/main.scss', filters='libsass', output='css/main.min.css')
    assets.register('css_all', css_bundle)

    return app
