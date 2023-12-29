Hello World to Containers with Flask

https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/ 

* Go to the developer directory:

    cd flask_docker

* Create a Image:

    docker build -t flask_docker:latest .

* Check to see if the image has been created:

    docker images

* Run a container from the image and test the app:

    docker run -d --publish 5000:5000 flask_docker:latest

* Using Postman use the following base URL:

    http://127.0.0.1:5000/