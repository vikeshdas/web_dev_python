
DEBUG = True

MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Vikeshdasvd@123'
MYSQL_DB = 'timbbadb'
# MYSQL_HOST = 'localhost'
MYSQL_HOST= 'mysql_service'
MYSQL_PORT = 3306

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
SQLALCHEMY_TRACK_MODIFICATIONS = False