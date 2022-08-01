FROM python:3.10-buster

RUN apt-get -y update
RUN apt-get -y install git
RUN pip3 install poetry

RUN mkdir /srv/www
#COPY integration_test.ini unit_test.ini /srv/www/
COPY poetry.lock pyproject.toml /srv/www/
WORKDIR /srv/www
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY ./democratizing/ /srv/www/democratizing/
