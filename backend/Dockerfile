FROM python:3.12-slim-bullseye

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . . 

EXPOSE 5000

CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:5000", "run:app"]