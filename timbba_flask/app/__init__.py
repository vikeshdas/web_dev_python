from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql
app = Flask(__name__)
pymysql.install_as_MySQLdb()


app.config.from_pyfile('config.py')
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


from app.views.user import user_bp
from app.views.client import client_bp
from app.views.role import role_bp

app.register_blueprint(user_bp)
app.register_blueprint(client_bp)
app.register_blueprint(role_bp)