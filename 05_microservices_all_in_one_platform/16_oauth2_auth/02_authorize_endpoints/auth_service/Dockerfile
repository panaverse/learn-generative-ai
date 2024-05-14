FROM python:3.12

LABEL maintainer="lahore-class"

WORKDIR /code

COPY . /code/

RUN pip install poetry

# RUN poetry config virtualenvs.create false
RUN poetry config virtualenvs.create false

# RUN poetry install
RUN poetry install --no-interaction --no-root


CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
