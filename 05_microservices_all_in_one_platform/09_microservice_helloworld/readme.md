# FastAPI Hello World

Follow the first part of this tutorial:

https://neon.tech/blog/deploy-a-serverless-fastapi-app-with-neon-postgres-and-aws-app-runner-at-any-scale

Create Project:

    poetry new fastapi-helloworld

Change directory to project:

    cd fastapi-helloworld 

Add dependecies:

    poetry add fastapi "uvicorn[standard]"

Write fastapi_helloworld/main.py

Run project in Poetry Envirnoment:

    poetry run uvicorn fastapi_helloworld.main:app --host 0.0.0.0 --port 8000

Open in Browser:

    http://0.0.0.0:8000/