from flask import Blueprint
main = Blueprint('main_bp', __name__)
from . import views, errors
