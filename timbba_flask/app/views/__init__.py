
from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/users')

from . import user

user_bp.add_url_rule('/', view_func=user.UserView.as_view('user'))
