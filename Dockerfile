FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /

COPY Pipfile Pipfile.lock /
RUN pip install pipenv && pipenv install --system

COPY . /

# WORKDIR /pj-scrape