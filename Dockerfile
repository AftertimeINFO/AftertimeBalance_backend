FROM python:3.10-slim

ENV POETRY_VIRTUALENVS_CREATE=false

RUN mkdir /app
#
WORKDIR /app
#
COPY poetry.lock .
COPY pyproject.toml .
# Need for psycopg2
RUN apt-get update
RUN apt-get -y install libpq-dev gcc
# Poetry installation
RUN pip install --upgrade pip
RUN pip install poetry
# Poetry configuration
#RUN poetry config virtualenvs.in-project true
#RUN poetry config virtualenvs.path .\.venv
RUN poetry install --no-root
RUN pip install gunicorn

COPY . .

CMD gunicorn api_service:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
#FROM debian:wheezy
#CMD ["/bin/ping", "localhost"]
#CMD ["/bin/bash"]
#ENTRYPOINT ["ls"]
#FROM ubuntu:latest
#RUN apt update -y
#ADD bash
#ENTRYPOINT ["sh"]