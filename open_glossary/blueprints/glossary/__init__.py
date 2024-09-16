from flask import Blueprint

glossary_bp = Blueprint('glossary', __name__)

from .views import *