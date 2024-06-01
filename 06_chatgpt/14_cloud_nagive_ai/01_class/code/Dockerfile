FROM jupyter/base-notebook:latest

WORKDIR /code

RUN pip install poetry

COPY . /code/

RUN poetry config virtualenvs.create false

RUN poetry install

EXPOSE 8888

CMD ["jupyter", "notebook" ,"--port", "8888", "--no-browser" ,"--allow-root"]

