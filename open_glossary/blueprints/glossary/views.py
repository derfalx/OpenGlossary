import string

from flask import render_template, abort, url_for

from . import glossary_bp
from ... import db
from ...database.entry import GlossaryEntry


@glossary_bp.route('/<string:current_filter>')
@glossary_bp.route('/')
def overview(current_filter: str = None):
    all_filter = [r[0] for r in db.session.query(GlossaryEntry.letter).distinct(GlossaryEntry.letter).all()]
    print(all_filter)
    if current_filter is None:
        current_filter = all_filter[0]

    if current_filter not in all_filter:
        abort(404)

    entries = db.session.query(GlossaryEntry).filter(GlossaryEntry.title.startswith(current_filter)).all()

    return render_template('glossary/overview.html',
                           active=all_filter.index(current_filter),
                           filters=all_filter,
                           entries=entries,
                           breadcrumb_paths=current_filter,
                           breadcrumb_titles=current_filter)


@glossary_bp.route('/details/<string:entry_title>')
def details(entry_title: str):
    entry = db.session.query(GlossaryEntry).filter_by(title=entry_title).first()
    if not entry:
        abort(404)

    return render_template('glossary/details.html',
                           entry=entry,
                           breadcrumb_paths=[
                               url_for('glossary.overview', current_filter=entry.title[0].upper()),
                               url_for('glossary.details', entry_title=entry.title)
                           ],
                           breadcrumb_titles=[
                               entry.title[0].upper(),
                               entry_title
                           ])
