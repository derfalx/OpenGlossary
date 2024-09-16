from flask import g
from flask_sqlalchemy import SQLAlchemy


def get_db():
    if 'database' not in g:
        g.db = SQLAlchemy(model_class=Base)
    return g.db