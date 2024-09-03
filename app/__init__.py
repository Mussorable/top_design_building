from flask import Flask
from flask_assets import Environment, Bundle

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
assets = Environment(app)

js_bundle = Bundle('js/main.js', filters='jsmin', output='js/main.min.js')

assets.register('js_all', js_bundle)

from app import routes, forms
