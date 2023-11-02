"""
    This file contains all the routes of the project. And configuration for the logger.
"""
from flask import Flask, logging
from flask_migrate import Migrate
import pymysql

from app.views.user import UserView,UsersView
from app.views.consignment import ConsignmentsView,ConsignmentView
from app.views.client import ClientView
from app.views.role import RoleView
from app.views.logs import LogsView,LogView
from .models import db
import logging

def create_app():
    app = Flask(__name__)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('logs/app.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

<<<<<<< Updated upstream
<<<<<<< Updated upstream
from app.views.routes import user_bp,users_bp
from app.views.routes import consignment_bp,consignments_bp
from app.views.routes import log_bp,logs_bp
from app.views.routes import client_bp
from app.views.routes import role_bp
=======
=======
>>>>>>> Stashed changes
    app.config.from_pyfile('config.py')
    pymysql.install_as_MySQLdb()
    db.init_app(app)
    Migrate(app, db)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

    app.add_url_rule("/log", view_func=LogView.as_view("log_view")) 
    app.add_url_rule("/logs", view_func=LogsView.as_view("logs_view")) 
    app.add_url_rule("/role", view_func=RoleView.as_view("role_view")) 
    app.add_url_rule("/users", view_func=UsersView.as_view("users_view"))  
    app.add_url_rule("/user", view_func=UserView.as_view("user_view"))
    app.add_url_rule("/client", view_func=ClientView.as_view("client_view"))
    app.add_url_rule("/consignment", view_func=ConsignmentView.as_view("consignment_view"))
    app.add_url_rule("/consignments", view_func=ConsignmentsView.as_view("consignments_view"))

    return app
