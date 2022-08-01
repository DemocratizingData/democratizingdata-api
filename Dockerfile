
FROM python:3.10-buster

EXPOSE 8000

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./src/ /app

WORKDIR /app
