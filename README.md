# admin-django

## Instructions

### Running

`docker-compose up`

### Migrating

Get into shell of docker container with:

`docker-compose exec backand sh`

Then run

`python manage.py makemigrations`

`python manage.py migrate`
