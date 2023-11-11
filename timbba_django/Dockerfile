FROM python:3


WORKDIR /app

COPY . /app/
RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh", "gunicorn", "-c", "gunicorn_config.py", "timbba.wsgi:application"]
