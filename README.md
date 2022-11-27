# Fake facebook website
This project is a fake facebook website using docker-compose.

if an error raise using this program please look at logs/errors.log
## Requirements 
- docker
- docker-compose

## To run this program on your machine
```git clone git@github.com:makan-dianka/fakebook.git```

```cd fakebook```

### Create file .env into web folder where is manage.py
set these values
- DEBUG=changeme
- EMAIL_HOST_USER="changeme"   here must be a google account. such @gmail.com
- EMAIL_HOST_PASSWORD="changeme" 

- HOST=db 
- PORT=3306
- NAME=phising
- USER_DB=root
- PASSWORD=root

- ALLOWED_HOSTS="changeme_in_production"

### Run docker-compose
```docker-compose --env-file ./.env up```

### Create superuser
```python manage.py createsuperuser```

If you want run this docker-compose in production, please look at docker-compose.yml and make 
a change if necessary.


