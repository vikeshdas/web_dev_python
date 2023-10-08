# from . import user_bp
# from ..models import Client

# class ClientView(MethodView):
#     def get(self):
#         print("reached here")
#         try:
#             users = Client.query.all()
#             user_list = [user.user_serializer() for user in users]

#             return jsonify({'users': user_list}), 200
#         except Exception as e:
#             return jsonify({'error': str(e)}), 500


# user_bp.add_url_rule('/users', view_func=ClientView.as_view('users'))


from flask.views import MethodView
from flask import request, jsonify, Blueprint
from app import db
from ..models import Client  

client_bp = Blueprint('client', __name__)

class ClientView(MethodView):
    def post(self):
        try:
            # Extract client data from the request JSON
            data = request.get_json()
            
            # Create a new client instance
            new_client = Client(
                name=data['name'],
                address=data['address'],
                contact=data['contact'],
                email=data['email']
            )
            
            # Add the client to the database session
            db.session.add(new_client)
            
            # Commit the changes to the database
            db.session.commit()
            
            return jsonify({'message': 'Client created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

# Register the ClientView class with the client_bp blueprint
client_bp.add_url_rule('/client', view_func=ClientView.as_view('clients'))
