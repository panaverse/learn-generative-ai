# Postgres Container

[How to Use the Postgres Docker Official Image](https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/)

[Postgres Released](https://www.postgresql.org/support/versioning/)

[PostgreSQL Cheat Sheet](https://www.postgresqltutorial.com/postgresql-cheat-sheet/)

Postgres’ object-relational structure and concurrency are advantages over alternatives like MySQL. And while no database technology is objectively the best, Postgres shines if you value extensibility, data integrity, and open-source software. It’s highly scalable and supports complex, standards-based SQL queries. 

1. Postgres Docker Official Image
   
   Specifically, Postgres is perfect for the following use cases:
   - Connecting Docker shared volumes to your application
   - Testing your storage solutions during development
   - Testing your database application against newer versions of your main application or Postgres itself


* Enter a quick pull command

    docker pull postgres:15.5

* Start a Postgres container

    docker run --name db_postgres_dev -e POSTGRES_PASSWORD=mysecretpassword -d postgres:15.5

* Interact with Postgres container

    docker exec -it -u postgres db_postgres_dev /bin/bash

* Login Postgres

    psql

* Logout from Postgres

    exit

* Logout from container

    exit

* Stop Postgres container

    docker stop db_postgres_dev

* Kill Postgres container

    docker rm db_postgres_dev

2. Run Postgres via Docker Compose

* Start a Postgres container

    docker-compose -f docker-compose.yml up -d

* Interact with Postgres container

    docker exec -it -u postgres db_postgres_dev /bin/bash

* Login Postgres

    psql

* Logout from Postgres

    exit

* Logout from container

    exit

3. Docker secrets

Docker secrets are only compatible with certain environment variables. [Reference our docs](https://github.com/docker-library/docs/blob/master/postgres/README.md#docker-secrets) to learn more.