
from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')
users_bp = Blueprint('users', __name__, url_prefix='/users')
consignment_bp=Blueprint('consignment', __name__, url_prefix='/consignment')
consignments_bp=Blueprint('consignments', __name__, url_prefix='/consignments')
log_bp=Blueprint('log', __name__, url_prefix='/log')
logs_bp=Blueprint('logs', __name__, url_prefix='/logs')
client_bp=Blueprint('client',__name__, url_prefix='/client')
role_bp=Blueprint('role',__name__, url_prefix='/role')

from app.views import user,consignment,logs,client,role

user_bp.add_url_rule('/', view_func=user.UserView.as_view('user'))
users_bp.add_url_rule('/', view_func=user.UsersView.as_view('users'))
consignment_bp.add_url_rule('/', view_func=consignment.ConsignmentView.as_view('consignment'))
consignments_bp.add_url_rule('/', view_func=consignment.ConsignmentsView.as_view('consignments'))
log_bp.add_url_rule('/', view_func=logs.LogView.as_view('log'))
logs_bp.add_url_rule('/', view_func=logs.LogsView.as_view('log_list'))
client_bp.add_url_rule('/',view_func=client.ClientView.as_view('client'))
role_bp.add_url_rule('/', view_func=role.RoleView.as_view('role'))
