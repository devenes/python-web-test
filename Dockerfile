FROM python:3.7-slim-buster

WORKDIR /usr/src/test/

COPY . ./

RUN pip install -r /usr/src/test/requirements.txt