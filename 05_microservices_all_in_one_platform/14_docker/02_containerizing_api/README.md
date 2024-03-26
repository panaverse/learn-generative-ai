# Containerizing the API

We will take the microservice created in step10_microserice_db and containerize it.

Now we will use the following Docker base image:

https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi


Note: If you are using Kubernetes or similar tools. In that case, you probably don't need this image (or any other similar base image). You are probably better off building a Docker image from scratch as explained in the docs for FastAPI in Containers - [Docker: Build a Docker Image for FastAPI](https://fastapi.tiangolo.com/deployment/docker/#replication-number-of-processes).

I have updated our toml file using this as a base:

https://github.com/tiangolo/full-stack-fastapi-template/blob/master/backend/pyproject.toml

Note: Review each and every dependency in the toml file.



We are using this Dockerfile template:

https://github.com/tiangolo/full-stack-fastapi-template/blob/master/backend/Dockerfile

Additional References:

https://www.jeffastor.com/blog/testing-fastapi-endpoints-with-docker-and-pytest/

Install dependency:

    poetry install

Run project in Poetry Envirnoment, to see if it is running outside a container:

    poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000

Open in Browser:

    http://0.0.0.0:8000/

    http://0.0.0.0:8000/docs

    http://0.0.0.0:8000/openapi.json

Run test:

    poetry run pytest



