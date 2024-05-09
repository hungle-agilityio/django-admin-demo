# # syntax=docker/dockerfile:1
# FROM python:3.11

# RUN   apt update && \
#       apt install -y default-libmysqlclient-dev gcc git pkg-config libxml2-dev libxmlsec1-dev libxmlsec1-openssl

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# RUN npm install
# COPY . /code/

# Use the official Node.js image as base
FROM node:latest

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY / ./