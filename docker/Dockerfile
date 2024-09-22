FROM python:3.12-bookworm
LABEL authors="falx"

EXPOSE 5050/tcp

RUN groupadd -r app && useradd -r -m -g app app

RUN apt update
RUN apt install -y curl

WORKDIR  /app
# Copy everything from the parent directory - except what's defined in .dockerignore
COPY .. .

RUN chown -R app:app /app

USER app
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN /home/app/.local/bin/poetry install


CMD ["/home/app/.local/bin/poetry", "run", "gunicorn", "-c", "/app/open_glossary/gunicorn_conf.py", "open_glossary:create_app()"]