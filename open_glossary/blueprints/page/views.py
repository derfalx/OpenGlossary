from flask import abort, render_template

from open_glossary import db
from open_glossary.blueprints.page import page_bp
from open_glossary.database.page import Page


@page_bp.route('/page/<string:page>')
def page(page: str):
    page = db.session.query(Page).filter(Page.name == page).first()
    if page is None:
        abort(404)
    return render_template('page/page.html', page=page)
