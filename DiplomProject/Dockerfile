FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip --no-cache-dir && \
    pip install --no-cache-dir poetry && \
    pip install django && \
    poetry install --no-interaction --no-ansi \

COPY . .