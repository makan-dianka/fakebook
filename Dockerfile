FROM python:3.8
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install vim -y

WORKDIR /var/www
COPY . .
WORKDIR /var/www/web
RUN chmod +x ./entrypoint.sh
RUN pip install --upgrade pip && pip install -r requirements.txt