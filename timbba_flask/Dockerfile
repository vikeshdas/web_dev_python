
FROM python:3

COPY . /timbba_flask/

WORKDIR /timbba_flask

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app:create_app
ENV FLASK_ENV=development

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
