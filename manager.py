from app import app, db, cli
from app.models import User

import sqlalchemy as sa
import sqlalchemy.orm as so


@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'sa': sa, 'so': so, 'db': db, 'User': User}
