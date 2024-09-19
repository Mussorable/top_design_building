import os
import sys
import click

from flask import Blueprint
from manager import COV

bp = Blueprint('cli', __name__, cli_group=None)


@bp.cli.group()
def translate():
    """ Translation and localization."""
    pass


@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language."""
    if os.system('pybabel extract -F babel.cfg -k _l -o languages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel init -i languages.pot -d app/translations -l ' + lang):
        raise RuntimeError('init command failed')
    os.remove('messages.pot')


@translate.command()
def update():
    """Update all languages."""
    if os.system('pybabel extract -F babel.cfg -k _l -o languages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i languages.pot -d app/translations'):
        raise RuntimeError('update command failed')
    os.remove('languages.pot')


@translate.command()
def compile():
    """Compile all languages."""
    if os.system('pybabel compile -d app/translations'):
        raise RuntimeError('compile command failed')


@bp.cli.command()
@click.option('--coverage/--no-coverage', default=False, help='Coverage Ticker app')
def test(coverage):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import unittest
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
