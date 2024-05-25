# Todo Codebase

**Running the application:**

With this Compose file saved as `compose.yml` , you can use the following commands to manage your application:

* `docker compose up -d`: This builds the images (if needed) and starts both containers in detached mode (background). You can check it by going open: http://host.docker.internal:8085/ in internal communication.
* `docker compose stop`: This stops both containers.
* `docker compose down`: This stops and removes both containers, as well as volumes associated with them.

## Connection String (added to the .env file)

Here's the connection string you can use to connect to the Postgres database from another container running in the same Docker network:


```
postgresql://ziakhan:my_password@PostgresCont:5432/mydatabase
```

Let's break down the connection string components:

* `postgresql://`: This specifies the database driver to be used (in this case, PostgreSQL).
* `ziakhan:my_password`: This defines the username and password for connecting to the database. Replace `my_password` with your actual Postgres user's password.
* `@PostgresCont`: This indicates the hostname or IP address of the Postgres container. By default, Docker links container names to hostnames within the Docker network. If your Postgres container is named differently (e.g., `my-postgres`), replace `PostgresCont` with the actual name.
* `:5432`: This specifies the port on which the Postgres server is listening. The default port for Postgres is 5432, but you can change it if your container configuration uses a non-standard port.
* `/mydatabase`: This defines the name of the specific database you want to connect to within the Postgres instance.

**Important Note:**

* Replace `mydatabase` with the actual name of the database you want to connect to.
* Ensure proper password storage is implemented for production environments. Avoid hardcoding the password in the connection string. Consider environment variables or secrets management solutions.

**Additional Considerations:**

* **Network Connectivity:** Verify that both containers are connected to the same Docker network to ensure proper communication.
* **Custom Ports:** If you've mapped the Postgres container's port to a different host port during container creation using `-p`, update the connection string's port number accordingly (e.g., `:5433` if mapped to host port 5433).

By following these guidelines and using the provided connection string format, you should be able to connect to your Postgres database from another container within your Docker environment.

## Install pgAdmin to connect to the Database

pgAdmin is the most popular and feature rich Open Source administration and development platform for PostgreSQL, the most advanced Open Source database in the world.

Download and Install pgAdmin 4:

https://www.pgadmin.org/download/

Connect to our PostgresSQL Container:

Host name/address: localhost

Post: 5433 (note it is not the default 5432)

Maintaince database: mydatabase

Username: ziakhan

Password: my_password

## Assignment

Create a seprate database container for testing in compose file. You dont need to even use a volume for test database since we don't care to persist test data between runs. Once you have created the test database and updated the .env file, run the tests.  


