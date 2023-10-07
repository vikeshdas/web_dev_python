# # from app import app, db
# from ..models import User
# from flask.views import MethodView
# from flask import (
#     Blueprint, jsonify, flash, request, redirect, url_for,
# )

# bp = Blueprint('/user', __name__)
# print("reached in file")
# class User(MethodView):
#     def get(self):
#         print("reached till USER")
#         try:
#             users = User.query.all()  # Restrieve all user records from the database
#             user_list = [user.user_serializer() for user in users]  # Serialize the users

#             return jsonify({'users': user_list}), 200  # Return the users as JSON response
#         except Exception as e:
#             return jsonify({'error': str(e)}), 500



# from ..models import User
# from flask.views import MethodView
# from flask import (
#     Blueprint, jsonify
# )

# # Remove the '/' in Blueprint, as it should be just 'user'
# bp = Blueprint('user', __name__)
# print("reached in file")

# class UserView(MethodView):
#     def get(self):
#         print("reached till USER")
#         try:
#             users = User.query.all()
#             user_list = [user.user_serializer() for user in users]

#             return jsonify({'users': user_list}), 200
#         except Exception as e:
#             return jsonify({'error': str(e)}), 500


from flask.views import MethodView
from flask import jsonify
from . import user_bp
from ..models import User

class UserView(MethodView):
    def get(self):
        print("reached here")
        try:
            users = User.query.all()
            user_list = [user.user_serializer() for user in users]

            return jsonify({'users': user_list}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500


user_bp.add_url_rule('/users', view_func=UserView.as_view('users'))
