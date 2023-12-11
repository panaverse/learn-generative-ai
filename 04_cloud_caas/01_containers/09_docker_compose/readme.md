# Docker Compose

[Docker Compose overview](https://docs.docker.com/compose/)

[Try Docker Compose](https://docs.docker.com/compose/gettingstarted/)

### Prerequisites

You need to have Docker Engine and Docker Compose on your machine. You can either:

- Install [Docker Engine](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) as standalone binaries
- Install [Docker Desktop](https://docs.docker.com/desktop/) which includes both Docker Engine and Docker Compose

Hello World to Containers with Flask

https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/ 

* Go to the developer directory:

    cd flask_docker

1. Define services in a Compose file

Create a file called ```compose.yaml``` in your project directory and paste the following:

```
version: '1.0'
services:
    web:
        build: .
        ports:
        - "5000:5000"
```

This Compose file defines web service

The web service uses an image that's built from the Dockerfile in the current directory. It then binds the container and the host machine to the exposed port, 5000. This example service uses the default port for the Flask web server, 5000.


2. Build and run your app with Compose

* From your project directory, start up your application by running docker compose up.

     docker compose up

* Using Postman use the following base URL:

    http://127.0.0.1:5000/


3. Edit the Compose file to add a bind mount

Edit the ```compose.yaml``` file in your project directory to add a [bind mount](https://docs.docker.com/storage/bind-mounts/) for the web service:

```
version: '1.0'
services:
    web:
        build: .
        ports:
        - "5000:5000"
        volumes:
        - type: bind
          source: .\        # For Linux, use / reverse slash to navigate to the current directory.
          target: /app
```

4. Re-build and run the app with Compose

From your project directory, type docker compose up to build the app with the updated Compose file, and run it.

    docker compose up