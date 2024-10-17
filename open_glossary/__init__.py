import json

from flask import Flask
from loguru import logger

from open_glossary.database import Base, db


def create_app():
    app = Flask(__name__)
    load_config(app)
    setup_db(app)
    register_blueprints(app)

    @app.context_processor
    def set_default_context():
        from open_glossary.database.entry import GlossaryEntry
        return dict(title='Zen Glossar',
                    entries_count=db.session.query(GlossaryEntry).count())

    return app


def setup_db(app):
    logger.info('Setting up database')
    db.init_app(app)

    logger.info('Creating tables if not exists')
    from .database.entry import GlossaryEntry
    with app.app_context():
        db.create_all()


def register_blueprints(app: Flask):
    logger.info('Registering blueprints')

    from .blueprints.glossary import glossary_bp
    app.register_blueprint(glossary_bp, url_prefix='/')

    from .blueprints.page import page_bp
    app.register_blueprint(page_bp, url_prefix='/')


def load_config(app: Flask):
    logger.info('Loading config')
    with open('./config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    app.config.update(config)
