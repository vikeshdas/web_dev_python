"""
  Database configuration file. The project is connected to the MySQL database.
  The below code describes the database name, user,password of the mysql database.
"""
DEBUG = True
import pymysql
import time
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'vikesh'
MYSQL_DB = 'flask_timbbadbs'
# MYSQL_HOST = 'localhost'
MYSQL_HOST= 'mysql_service'
MYSQL_PORT = 3306

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

connection_check = True
while connection_check:
    try:
        connection = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
        print("successfully created connection")
        connection_check = False
    except pymysql.OperationalError as e:
        print(f"Error: {e}. Retrying in 3 seconds...")
        time.sleep(3)
