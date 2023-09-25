from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
app = Flask(__name__)
pymysql.install_as_MySQLdb()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Vikeshdasvd@123@localhost/timbbadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

<<<<<<< HEAD
from app.views.user import user_bp

app.register_blueprint(user_bp)
=======
from app.user import bp as user_bp

app.register_blueprint(user_bp)  

>>>>>>> a14fa3acf6bb6ac0bc78890b9a921c7146a605e4
