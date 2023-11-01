FROM python:3

COPY . /timbba_flask/

WORKDIR /timbba_flask

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app:create_app
ENV FLASK_ENV=development

CMD ["gunicorn", "-c", "gunicorn_config.py", "app:create_app()"]

