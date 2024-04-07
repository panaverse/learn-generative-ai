# Docker Compose with Database Service

To validate your compose.yaml file give the following command (docker compose config renders the actual data model to be applied on the Docker Engine. It resolves variables in the Compose file, and expands short-notation into the canonical format):

  docker compose config

**Example: Python and PostgreSQL with Network**

This example demonstrates a Compose file with a Python service and a PostgreSQL service connected by a custom network named "my-api-net":

Details

https://hub.docker.com/_/postgres

https://github.com/docker-library/docs/blob/master/postgres/README.md


```yaml
version: "3.9"  # Specify the Docker Compose version

services:
  python-app:
    build: .  # Build the image from the current directory (Dockerfile needed)
    ports:
      - "5000:5000"  # Expose container port 5000 to host port 5000
    environment:
      - DATABASE_HOST: postgres  # Set environment variable for DB connection
    networks:
      - my-app-net

  postgres:
    image: postgres:latest  # Use the official PostgreSQL image
    environment:
      - POSTGRES_PASSWORD: my_password  # Set password for PostgreSQL
    volumes:
      - postgres_data:/var/lib/postgresql/data  # Persist data volume
    networks:
      - my-app-net

networks:
  my-app-net:  # Define the custom network
```

**Explanation:**

* **version:** This specifies the Docker Compose file version (here, version 3.9).
* **services:** This section defines two services:
    * `python-app`: This builds a container image from the current directory (assuming a Dockerfile exists). It exposes port 5000 and sets an environment variable `DATABASE_HOST` to connect to the PostgreSQL service using the service name `postgres`. It also connects to the `my-app-net` network.
    * `postgres`: This uses the official `postgres:latest` image and sets an environment variable for the password. It defines a volume named `postgres_data` to persist the database data. This service also connects to the `my-app-net` network.
* **networks:** This section defines a custom network named `my-app-net`. This allows the services to communicate with each other using container names instead of needing to know IP addresses.

**Running the application:**

With this Compose file saved as `compose.yml` , you can use the following commands to manage your application:

* `docker-compose up -d`: This builds the images (if needed) and starts both containers in detached mode (background).
* `docker-compose stop`: This stops both containers.
* `docker-compose down`: This stops and removes both containers, as well as volumes associated with them.

## Connection String

Here's the connection string you can use to connect to the Postgres database from another container running in the same Docker network:

```
postgresql://postgres:password@postgres:5432/mydatabase
```

Let's break down the connection string components:

* `postgresql://`: This specifies the database driver to be used (in this case, PostgreSQL).
* `postgres:password`: This defines the username and password for connecting to the database. Replace `password` with your actual Postgres user's password.
* `@postgres`: This indicates the hostname or IP address of the Postgres container. By default, Docker links container names to hostnames within the Docker network. If your Postgres container is named differently (e.g., `my-postgres`), replace `postgres` with the actual name.
* `:5432`: This specifies the port on which the Postgres server is listening. The default port for Postgres is 5432, but you can change it if your container configuration uses a non-standard port.
* `/mydatabase`: This defines the name of the specific database you want to connect to within the Postgres instance.

**Important Note:**

* Replace `mydatabase` with the actual name of the database you want to connect to.
* Ensure proper password storage is implemented for production environments. Avoid hardcoding the password in the connection string. Consider environment variables or secrets management solutions.

**Additional Considerations:**

* **Network Connectivity:** Verify that both containers are connected to the same Docker network to ensure proper communication.
* **Custom Ports:** If you've mapped the Postgres container's port to a different host port during container creation using `-p`, update the connection string's port number accordingly (e.g., `:5433` if mapped to host port 5433).

By following these guidelines and using the provided connection string format, you should be able to connect to your Postgres database from another container within your Docker environment.
