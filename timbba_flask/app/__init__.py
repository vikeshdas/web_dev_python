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
from app.views.user import users_bp
from app.views.client import client_bp
from app.views.role import role_bp
from app.views.consignment import consignment_bp
from app.views.consignment import consignments_bp
from app.views.logs import log_bp
from app.views.logs import logs_bp

app.register_blueprint(users_bp)
app.register_blueprint(user_bp)
app.register_blueprint(role_bp)
app.register_blueprint(consignment_bp)
app.register_blueprint(consignments_bp)
app.register_blueprint(log_bp)
app.register_blueprint(logs_bp)
app.register_blueprint(client_bp)