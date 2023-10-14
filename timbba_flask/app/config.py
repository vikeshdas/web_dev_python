
# DEBUG = True
import pymysql
import time
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = 'vikesh'
# MYSQL_DB = 'flask_timbbadb'
# # MYSQL_HOST = 'localhost'
# MYSQL_HOST= 'mysql_service'
# MYSQL_PORT = 3306

# SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
# SQLALCHEMY_TRACK_MODIFICATIONS = False

while True:
    try:
        db = pymysql.connect(host='mysql_service', user='root', password='vikesh', db='flask_timbbadb')
        break  # Connection successful, exit the loop
    except pymysql.OperationalError as e:
        print(f"Error: {e}. Retrying in 5 seconds...")
        time.sleep(5)