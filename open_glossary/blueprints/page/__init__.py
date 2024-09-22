from flask import Blueprint

page_bp = Blueprint('page', __name__)

from .views import *