# Hello World to Containers for Developers

[Read Pages 32-36 of our Text Book: Docker Deep Dive by Nigel Poulton 2023 Edition](https://www.amazon.com/Docker-Deep-Dive-Nigel-Poulton/dp/1916585256)

## Basic Flask App

We will first create basic Flask Web App.

Reference:

https://flask.palletsprojects.com/en/3.0.x/quickstart/

1. Create a directory named "web"
2. cd web
3. Write a simple Flask App in web/app.py that creates a simple Flask application that returns “Hello from Zia!” when the root path is accessed.
4. Install dependencies

    ```pip install -r requirements.txt```
5. Run

    ```python -m flask run``` 
6. Open in browser:
    http://127.0.0.1:5000

## Containerize the App

Now we will create a Dockerfile for our Flask Application. A Dockerfile is a file that contains instructions on how to build your image. It describes the entire process of building your image from the installation of your Python app to the creation of your container.

1. Create a file named Dockerfile under the project web directory. This is the file docker reads instructions to build image.
2. Build the Docker Image:
    docker build -t flask-app:latest .
3. Check if the image was created by listing the images:
    docker images
4. Run the Docker Container
    docker run -p 5000:5000 flask-app
5. Check to see if the container is running:
    docker ps
6. Open in browser:
    http://127.0.0.1:5000

