#!/bin/sh
wait_for_mysql() {
  until python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(('mysql_service', 3306))" >/dev/null 2>&1
  do
    echo "Waiting for MySQL service to start..."
    sleep 5
  done
}

wait_for_mysql

python manage.py makemigrations timbba
python manage.py migrate timbba

exec "$@"
