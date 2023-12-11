# Dockerfile Details

To build a Docker image, you need to create a Dockerfile. It is a plain text file with instructions and arguments. 

docker build is the command that reads a Dockerfile and containerizes an application. 

The -t flag tags the image, and the -f flag lets you specify the name and location of the Dockerfile. 

With the -f flag, you can use a Dockerfile with an arbitrary name and in an arbitrary location. The build context is where
your application files exist and can be a directory on your local Docker host or a remote Git repo.

## The Dockerfile Commands

Here is the description of the instructions we’re going to use in our next example:

FROM — set base image

The Dockerfile FROM instruction specifies the base image for the new image you’re building. It’s usually the first instruction in a Dockerfile and a bestpractice is to use images from official repos on this line. FROM is also used to distinguish a new build stage in multi-stage builds.

RUN — execute command in container

The Dockerfile RUN instruction lets you to run commands inside the image during a build. It’s commonly used to update packages and install dependencies. Each RUN instruction adds a new layer to the overall image.

COPY

The Dockerfile COPY instruction adds files into the image as a new layer. It’s common to use it to copy your application code into an image.

ENV — set environment variable

EXPOSE

The Dockerfile EXPOSE instruction documents the network port an application uses.

WORKDIR — set working di    rectory

VOLUME — create mount-point for a volume

CMD — set executable for container

This CMD instruction is used to define what command the container should execute when launched.

ENTRYPOINT

The Dockerfile ENTRYPOINT instruction sets the default application to run when the image is started as a container. The ENTRYPOINT instruction works very similarly to CMD in that it is used to specify the command executed when the container is started. However, where it differs is that ENTRYPOINT doesn't allow you to override the command. Instead, anything added to the end of the docker run command is appended to the command. 

Some other Dockerfile instructions include LABEL, ONBUILD, HEALTHCHECK, and more.


## Best practices for creating images

Include only necessary context – use a .dockerignore file (like .gitignore in git)

Avoid installing unnecessary packages – it will consume extra disk space

Use [environment variables](https://docs.docker.com/engine/reference/builder/#environment-replacement) (in RUN, EXPOSE, VOLUME). It will make your Dockerfile more flexible



