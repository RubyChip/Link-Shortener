FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /code/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./entrypoint.sh . 
COPY /alembic/ /code/alembic/
COPY ./alembic.ini .
COPY ./app /code/app

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/code/entrypoint.sh" ]
