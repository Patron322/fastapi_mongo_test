FROM python:3.10-slim as backend
WORKDIR /code

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && pip install --upgrade pip
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root


COPY src .
COPY ./.env /code/settings
