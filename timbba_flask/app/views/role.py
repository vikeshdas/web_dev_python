from flask.views import MethodView
from flask import request, jsonify, Blueprint
from app import db
from ..models import Roles  

role_bp = Blueprint('client', __name__)

class RoleView(MethodView):
    def post(self):
        try:
            data = request.get_json()
            
            new_item = Roles(
                role_name=data['name'],
            )
            
            db.session.add(new_item)
            
            db.session.commit()
            
            return jsonify({'message': 'Role created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
role_bp.add_url_rule('/role', view_func=RoleView.as_view('role'))