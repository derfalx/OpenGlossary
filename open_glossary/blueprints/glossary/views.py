import string

from flask import render_template, abort

from . import glossary_bp
from ... import db
from ...database.entry import GlossaryEntry


@glossary_bp.route('/<string:current_filter>')
@glossary_bp.route('/')
def overview(current_filter: str = None):
    all_filter = list(string.ascii_uppercase)
    if current_filter is None:
        current_filter = 'A'

    if current_filter not in all_filter:
        abort(404)

    entries = db.session.query(GlossaryEntry).filter(GlossaryEntry.title.startswith(current_filter)).all()

    return render_template('glossary/overview.html',
                           active=all_filter.index(current_filter),
                           filters=all_filter,
                           entries=entries)

@glossary_bp.route('/details/<string:entry_title>')
def details(entry_title: str):
    entry = db.session.query(GlossaryEntry).filter_by(title=entry_title).first()
    if not entry:
        abort(404)

    return render_template('glossary/details.html',
                           entry=entry)
