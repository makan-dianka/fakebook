FROM python:3.8
ENV PYTHONUNBUFFERED=1

# RUN apt-get update && apt-get install vim -y

WORKDIR /var/www
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt