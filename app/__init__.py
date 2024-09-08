from flask import Flask
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

assets = Environment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

js_bundle = Bundle('js/main.js', filters='jsmin', output='js/main.min.js')
assets.register('js_all', js_bundle)

css_bundle = Bundle('css/main.scss', filters='libsass', output='css/main.min.css')
assets.register('css_all', css_bundle)

from app import routes, forms, models
