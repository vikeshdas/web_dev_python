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


from app.views.routes import user_bp,users_bp
from app.views.routes import consignment_bp,consignments_bp
from app.views.routes import log_bp,logs_bp
from app.views.routes import client_bp
from app.views.routes import role_bp

app.register_blueprint(users_bp)
app.register_blueprint(user_bp)
app.register_blueprint(role_bp)
app.register_blueprint(consignment_bp)
app.register_blueprint(consignments_bp)
app.register_blueprint(log_bp)
app.register_blueprint(logs_bp)
app.register_blueprint(client_bp)