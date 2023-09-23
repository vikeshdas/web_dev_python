from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
app = Flask(__name__)
pymysql.install_as_MySQLdb()
# Configure the MySQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Vikeshdasvd@123@localhost/timbbadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress a warning
db = SQLAlchemy(app)

# Import and register your Blueprints
from app.user import bp as user_bp

app.register_blueprint(user_bp)  # Replace with your desired prefix

# Other app configurations and extensions...
