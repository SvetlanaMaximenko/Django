FROM python:3.11-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip --no-cache-dir && \
    pip install --no-cache-dir poetry && \
    poetry install --no-interaction --no-ansi

COPY . .