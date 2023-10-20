from app import app, db

from flask.views import MethodView
from flask import jsonify,request

from . import user_bp
from . import users_bp

from ..models import User,Client

class UsersView(MethodView):
    """
      A view class handles operations related to more than one user.like get information of all users related to a client.

      Methods:
        get(self,request): get information of all users of a client

    """
    def get(self):
        """
            Fetch all users of a client based on client_id .if client exist in database

            Args:
                request: HttpRequest's object contains client_id whose all user need to fetch from database.
            
            Return: information of all user of a client in the JSON format or error if client is invalid.
                
        """
        try:
            data=request.get_json()
            clien_id = data.get('client_id')
            client=Client.query.get(clien_id)
            if not client:
                return jsonify({"client not found"}),404
            
            users = User.query.filter(client_id=clien_id).all()
            user_list = [user.user_serializer() for user in users]

            return jsonify({'users': user_list}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500


class UserView(MethodView):
    """
        A View class to handle user related operations like creating a new user,fetching information of a user , 
        updating a user and delete a user.

    """
    def get(self):
        """
            Fetch information of a user from database, based on user_id.

            Args:
                request: HttpRequest's object contains id of a user.
            
            Returns: JsonResponse: returns information of a user in the JSON format.
        """
        try:
            data = request.get_json()
            user = User.query.get(data.get("user_id"))
            
            if not user:
                return jsonify({'error': 'User not found'}), 404

            user_data = {
                'name': user.name,
                'username': user.username,
                'role_id': user.role_id,
                'contact': user.contact,
                'client_id': user.client_id
            }

            return jsonify(user_data), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    
    def put(self):
        """
            Creating a new user with unique username and contact number,means saving information of a user in databse.

            Args:
                request:HttpRequest's object contains information of a user to save in database.
            
            Returns:
                JsonResponse : Returns message in JSON format either data saved successfully or failed.
        """
        try:
            data = request.get_json()
            username=data.get('username')
            contact=data.get('contact')
            duplicate_username = User.query.filter_by(username=username).first()
            contact_duplicate= User.query.filter_by(contact=contact).first()

            if duplicate_username:
                return jsonify({'error': 'username already exist'}), 404
            if contact_duplicate:
                return jsonify({'error': 'User already exist with this contact number'}), 404
            
            new_user = User(
            name = data.get('name'),
            username = data.get('username'),
            role_id = data.get('role_id'),
            contact = data.get('contact'),
            client_id = data.get('client_id'),
            )

            db.session.add(new_user)
            db.session.commit()

            return jsonify({'message': 'User added successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    

    def patch(self):
        """
            Update information of a user based on id of a user.

            Args:
                request:HttpRequest's object contains id of a user.
            
            Returns(JsonResponse): returns a message in Json format either successfully updated or error.
        """
        try:
            data = request.get_json()
            user_id=data.get("user_id")
            client_id=data.get("client_id")
            
            user = User.query.get(user_id)
            client=User.query.get(client_id)
            if not user:
                return jsonify({'error': 'User not found'}), 404
            if not client:
                return jsonify({'error': 'Client not found'}), 400
            
            user.name = data.get('name', user.name)
            user.username = data.get('username', user.username)
            user.role_id = data.get('role_id', user.role_id)
            user.contact = data.get('contact', user.contact)

            db.session.commit()

            return jsonify({'message': 'User updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def delete(self):
        """
            Delete a user from databse based on user_id.

            Args:
                HttpRequest's object contains id of a user, whose information needs to delete.
            
            Returns: returns message in JSON format either user deleted successfully or error.
        """
        try:
            data = request.get_json()
            user_id=data.get("user_id")
            user = User.query.get(user_id)

            if not user:
                return jsonify({'error': 'User not found'}), 404

            db.session.delete(user)
            db.session.commit()

            return jsonify({'message': 'User deleted successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

user_bp.add_url_rule('/users', view_func=UsersView.as_view('users'))
users_bp.add_url_rule('/user', view_func=UserView.as_view('user'))