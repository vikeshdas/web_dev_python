FROM python:3
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE timbba.settings

WORKDIR /app

COPY . /app/
RUN pip install -r requirements.txt
RUN pip install gunicorn
EXPOSE 8000

# CMD ["gunicorn", "timbba.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD ["gunicorn", "-c", "gunicorn_config.py", "timbba.wsgi:application"]
