
from flask.views import MethodView
from flask import request, jsonify
from app.models import db
from datetime import datetime
from app.models import Client


class ClientView(MethodView):
    """
        A view for handling client related operation like creating a new client.
        A client is a admin who buys subscription for our application or we can 
        say that client is a owner of a factory who makes logs to plyboard.
    """
    def put(self):
        """
            Create a new client.This function will be required when a client buys subscription.
            When client signup then this function will be executing.

            Args:
                HttpRequest :Contains client data in request body.

            Returns:
                JsonResponse:return JSON, that client is created successfully. 
        """
        try:
            data = request.get_json()
            duplicate_client=Client.query.filter_by(contact=data.get('contact')).first()
<<<<<<< Updated upstream
            
=======
            print("DUPLICATE CLIENT",duplicate_client)
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
=======

>>>>>>> Stashed changes
