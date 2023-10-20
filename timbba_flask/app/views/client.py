
from flask.views import MethodView
from flask import request, jsonify
from app import db
from datetime import datetime
from ..models import Client  

from . import client_bp
# client_bp = Blueprint('client', __name__)

class ClientView(MethodView):
    def put(self):
        try:
            data = request.get_json()
            duplicate_client=Client.query.filter_by(contact=data.get('contact'))
            if duplicate_client:
                return jsonify({'error': 'Duplicate client'}), 404
            new_client = Client(
                name=data['name'],
                address=data['address'],
                contact=data['contact'],
                email=data['email'],
                updated_at=datetime.now()
            )

            db.session.add(new_client)
 
            db.session.commit()
            
            return jsonify({'message': 'Client created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

client_bp.add_url_rule('/client', view_func=ClientView.as_view('client_'))
