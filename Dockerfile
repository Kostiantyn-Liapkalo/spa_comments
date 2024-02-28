FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
EXPOSE 8000
WORKDIR /app
ENV PYTHONUNBUFFERED=true
WORKDIR /code
FROM python as poetry
ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN apt-get install gcc curl make automake g++\
      && curl -sSL https://install.python-poetry.org | python3 - \
      && apt-get clean -y curl

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi -vvv
FROM poetry as runtime
# Run server
ENTRYPOINT [ "python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]