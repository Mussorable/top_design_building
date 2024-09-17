from flask import render_template, current_app
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template(
        'errors/404.html',
        title=f'{current_app.config['TITLE']} (404)',
        header_image='new_apartment',
        is_under_header_caption=True
    ), 404


@bp.app_errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return render_template(
        'errors/500.html',
        title=f'{current_app.config['TITLE']} (500)',
        header_image='new_apartment',
        is_under_header_caption=True
    ), 500
