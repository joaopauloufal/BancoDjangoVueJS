#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Esperando pelo servico do postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL iniciado"
fi

cp -r ./banco_django_vuejs_api/.env.dev.example ./banco_django_vuejs_api/.env
python manage.py migrate
python manage.py initadmin

exec "$@"