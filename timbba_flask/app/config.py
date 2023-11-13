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

