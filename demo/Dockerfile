# syntax=docker/dockerfile:1
FROM python:3.12

RUN   apt update && \
      apt install -y default-libmysqlclient-dev gcc git pkg-config libxml2-dev libxmlsec1-dev libxmlsec1-openssl

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN npm install
COPY . /code/
