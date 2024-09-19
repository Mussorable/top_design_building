import os

from app import create_app, db
from app.models import User

import sqlalchemy as sa
import sqlalchemy.orm as so

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage

    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User}
