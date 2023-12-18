# Volumes and Persistent Data

[Read Pages 185-193 of our Text Book: Docker Deep Dive by Nigel Poulton 2023 Edition](https://www.amazon.com/Docker-Deep-Dive-Nigel-Poulton/dp/1916585256)


[Docker Volumes](https://docs.docker.com/storage/volumes/)

[Bind mounts](https://docs.docker.com/storage/bind-mounts/)


There are two main categories of data — persistent and non-persistent.

Persistent is the data we need to keep. Things like customer records, financial data, research results, audit logs, and even some types of application log data. Non persistent is the data we don’t need to keep.

Both are important, and Docker has solutions for both.

To deal with non-persistent data, every Docker container gets its own non-persistent storage. This is automatically created for every container and is tightly coupled to the lifecycle of the container. As a result, deleting the container will delete the storage and any data on it.

To deal with persistent data, containers need to store it in a volume. Volumes are separate objects that have their lifecycles decoupled from containers. This means you can create and manage volumes independently, and they don’t get deleted when their container is deleted.

<img src="./EphemeralContainerStorage.png" alt="Ephemeral Container Storage" style="width:400px;"/>


Each writable container layer exists in the filesystem of the Docker host and you’ll hear it called various names. These include local storage, ephemeral storage, and graphdriver storage. It’s typically located on the Docker host in these locations:

- Linux Docker hosts: ```/var/lib/docker/<storage-driver>/...```
- Windows Docker hosts: ```C:\ProgramData\Docker\windowsfilter\...```

Containers and persistent data

Volumes are the recommended way to persist data in containers. There are three major reasons for this:

- Volumes are independent objects that are not tied to the lifecycle of a container
- Volumes can be mapped to specialized external storage systems
- Volumes enable multiple containers on different Docker hosts to access and share the same data

<img src="./High-level-view-of-volumes-and-containers.png" alt="High-level View of Volumes And Containers" style="width:400px;"/>

## Volumes

* Create a new volume called myvol.
        
        docker volume create myvol

<img src="./Plugging external storage into Docker.png" alt="Plugging external storage into Docker" style="width:400px;"/>

* List volumes
        
        docker volume ls

        docker volume inspect myvol

* There are two ways to delete a Docker volume:

        docker volume prune
        
        docker volume rm

* As the myvol volume is not in use, delete it with the prune command.
        
        docker volume prune


* Be sure to use the C:\ProgramData\Docker\volumes\bizvol\_data directory if you’re following along on Windows. Also, this step won’t work on Docker Desktop because Docker Desktop runs your entire Docker environment inside a VM.

        ls -l /var/lib/docker/volumes/bizvol/_data/

Sharing storage across cluster nodes

Integrating external storage systems with Docker makes it possible to share volumes between cluster nodes.As an example, a single storage LUN or NFS share can be presented to multiple Docker hosts.

<img src="./Sharing storage across cluster nodes.png" alt="Sharing storage across cluster nodes" style="width:400px;"/>

Volume drivers

<img src="./VolumeDrivers.png" alt="Volume Drivers" style="width:400px;"/>


## Bind mounts

Bind mounts have limited functionality compared to volumes. When you use a bind mount, a file or directory on the host machine is mounted into a container. The file or directory is referenced by its absolute path on the host machine. By contrast, when you use a volume, a new directory is created within Docker's storage directory on the host machine, and Docker manages that directory's contents.

<img src="./bind-mounts.png" alt="Bind Mounts" style="width:400px;"/>

New users should use the --mount syntax. Experienced users may be more familiar with the -v or --volume syntax, but are encouraged to use --mount, because research has shown it to be easier to use.

* The --mount and -v examples have the same result.

``` docker run -d -it  --mount type=bind, source="$(pwd)"/target, target=/app panacloud/test:latest ```

``` docker run -d -it -v "$(pwd)"/target:/app:z panacloud/test:latest ```