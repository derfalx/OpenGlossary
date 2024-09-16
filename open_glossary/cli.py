import click
from flask.cli import FlaskGroup

from open_glossary import create_app, db
from open_glossary.database.parser import MDToDBParser


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    app = create_app()
    with app.app_context():
        p = r'L:\Vault\Thoughts\Zen\Glossar\Shihô.md'
        parser = MDToDBParser(db)
        entry = parser.md_to_db(p)


