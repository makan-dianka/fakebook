FROM python:3.8

RUN apt-get update && apt-get install vim -y

WORKDIR /var/www
RUN python -m venv .venv