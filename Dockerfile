FROM python:3.8-slim-buster as base

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .


FROM base as developer
