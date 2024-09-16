from flask import Flask
from loguru import logger

from open_glossary.database import Base, db


def create_app():
    app = Flask(__name__)

    setup_db(app)
    register_blueprints(app)
    @app.context_processor
    def set_title():
        return dict(title='Zen Glossar')

    return app

def setup_db(app):
    logger.info('Setting up database')
    app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///D:\Code\OpenGlossary\glossary.db'
    db.init_app(app)

    logger.info('Creating tables if not exists')
    from .database.entry import GlossaryEntry
    with app.app_context():
        db.create_all()


def register_blueprints(app: Flask):
    logger.info('Registering blueprints')
    from .blueprints.glossary import glossary_bp
    app.register_blueprint(glossary_bp, url_prefix='/')
