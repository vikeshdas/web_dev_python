
FROM python:3
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app
ENV FLASK_ENV=development

# CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "-c", "gunicorn_config.py", "app:app"]
