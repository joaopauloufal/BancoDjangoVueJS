FROM python:3.8.5-alpine

WORKDIR /usr/src/app/banco_django_vuejs_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev bash

RUN pip install --upgrade pip
COPY ./banco_django_vuejs_api/requirements.txt .
RUN pip install -r requirements.txt

COPY ./banco_django_vuejs_api/banco_django_vuejs_api/.env.dev.example ./banco_django_vuejs_api/banco_django_vuejs_api/.env
COPY ./.docker/entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/.docker/entrypoint.sh"]