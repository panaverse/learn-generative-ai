# Deploy Streamlit App using Docker

https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker

* Cloned the Repo from this URL to streamlit-app/app dir:

https://github.com/streamlit/streamlit-example.git

* Go to the developer directory:

    cd streamlit-app

* add a Dockerfile in the root of the app

* Create a Image:

    docker build -t streamlit:latest .

* Check to see if the image has been created:

    docker images

* Run a container from the image and test the app:

    docker run -p 8501:8501 streamlit

* Open the browser on the following URL:

    http://localhost:8080/





