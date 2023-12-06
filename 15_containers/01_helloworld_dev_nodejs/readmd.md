# Hello World to Containers from Developers

[Read Pages 32-36 of our Text Book: Docker Deep Dive by Nigel Poulton 2023 Edition](https://www.amazon.com/Docker-Deep-Dive-Nigel-Poulton/dp/1916585256)

* Go to the developer directory:

    cd psweb

* Create a Image:

    docker build -t test:latest .

* Check to see if the image has been created:

    docker images

* Run a container from the image and test the app:

    docker run -d --name web1 --publish 8080:8080 test:latest

* Open the browser on the following URL:

    http://localhost:8080/