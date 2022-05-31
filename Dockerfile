FROM python:3.7-slim-buster

ADD ./requirements.txt /usr/src/test/requirements.txt

RUN pip install -r /usr/src/test/requirements.txt