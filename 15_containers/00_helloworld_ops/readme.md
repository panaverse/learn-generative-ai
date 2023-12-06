# Hello World Container Operations

1. Overview
[Read Chapters 1 and 2 of our Text Book: Docker Deep Dive by Nigel Poulton 2023 Edition](https://www.amazon.com/Docker-Deep-Dive-Nigel-Poulton/dp/1916585256)

2. Installing Docker Desktop (Chapter 3)

https://docs.docker.com/get-docker/

    docker version

Test Docker Installation:

    docker run hello-world

For Mac, if docker command not running:

https://stackoverflow.com/questions/64009138/docker-command-not-found-when-running-on-mac

https://www.insightsjava.com/2022/01/how-to-create-bash-profile-on-mac.html

3. Play with Docker

Play with Docker (PWD) is a fully functional internet-based Docker playground that lasts for 4 hours. You can add multiple nodes and even cluster them in a swarm.

https://labs.play-with-docker.com/

4. The Big Picture (Chapter 4)

https://docs.anaconda.com/free/anaconda/applications/docker/

https://hub.docker.com/r/continuumio/anaconda3

* Pull Anaconda Image:

    docker pull continuumio/anaconda3

* List the Images:

    docker images

* Launch the Container:

    docker run -it continuumio/anaconda3:latest /bin/bash

Note: You’ll see that the shell prompt has changed. This is because the -it flags switch your shell into the terminal
of the container — your shell is now inside of the new container!

* List Envirnoments:

    conda env list

* Check Python Version:

    python --version

* List all running processes:

    ps -elf

* Exit the Container without terminating it:

    Press Ctrl-PQ to exit the container without terminating it.

* List All Running Containers:

    docker ps

* Attaching to running Container:

    docker exec -it container_name bash

* Stop the Container:

    docker stop container_name

* List the Containers, even those that are in stopped state:

    docker ps -a

* Kill the Container:

    docker rm container_name

### TestContainers

[Adopting Testcontainers for local development](https://www.youtube.com/watch?v=he6Mtn3xCNU)

[Locally Test Your Serverless Applications with Test Containers](https://www.youtube.com/watch?v=z0F9tofV_MQ)

https://testcontainers.com/

### Localstack

https://www.localstack.cloud/

https://medium.com/agorapulse-stories/how-to-unit-test-aws-services-with-localstack-and-testcontainers-1d39fe5dc6c2 




