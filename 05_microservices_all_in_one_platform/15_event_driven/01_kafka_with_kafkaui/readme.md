# Kafka UI and Kafka Hello World

Here we will run Kafka with Kafka UI using Docker Compose.

- Step 1: Create new folder and copy compose.yml file from this step.

- Step 2: In Terminal at same path where compose.yml file is present run these commands:
    - `docker compose config` - to Validate our Compose file
    - `docker compose up --build` - this will run Kafka Container and Kafka UI Container.

- Step 3: Open http://localhost:8080 in browser

- Step 4: CREATE NEW TOPIC: 
    - Go to topics in left sidebar and then 
    - click on + Add a Topic Button in right top side of screen
    - create a new topic    
        * Topic Name: `topic1`
        * Number if Partitions: 1

- Step 5: ADD MESSAGES TO TOPIC FROM KAFKA UI
    - From Sidebar click on topics
    - Select topic1
    - Now on top-right side click on `Produce Message` button
    - Write Some Messages i.e: KEY: message1, VALUE: message1-hello etc.

- Step 6: Listen to Messages using Consumer
    - Firstly we will setup consumer and listen to messages in terminal
    - In Terminal Run:
        - `docker ps`
        - `docker exec -it -u root kafka /bin/bash`
        - `cd /opt/bitnami/kafka/bin` and view all scripts `ls`
        - Create A New Consumer 
        ```/opt/bitnami/kafka/bin/kafka-console-consumer.sh --topic topic1 --from-beginning --bootstrap-server localhost:9092```
        
        After running Above My Terminal Shows:
        ```
        root@5d0319939280:/opt/bitnami/kafka/bin# /opt/bitnami/kafka/bin/kafka-console-consumer.sh --topic topic1 --from-beginning --bootstrap-server localhost:9092
        message1-hello
        ```

- Step 7: Write a few more events/messages and view them in terminal. Next you can view this consumer in Kafka UI Consumers Tab from left sidebar.

Now in Browser play with the Kafka UI and revise the concepts of 
1. Kafka Broker
2. Topics
3. Producer
4. Messages (Asynchronous Events)
5. Consumers

## Breakdown of compose.yml file

The provided docker-compose.yml file defines a multi-container Docker environment that includes a Kafka broker setup in KRaft (Kafka Raft) mode and a Kafka UI component. 

KRaft mode is a more recent Kafka configuration that eliminates the need for Zookeeper by using an internal Raft protocol for consensus. 

Let's break down the file step by step:

### A. Kafka Service

#### 1. Image Specification:

- image: bitnami/kafka:3.6.2-debian-12-r3
- This line specifies the Docker image to use for the Kafka service. The image is from Bitnami, one of the latest version.

#### 2. Container Name:

- container_name: kafka
- This assigns a specific name to the running container, making it easier to reference.

#### 3. Command:

- The command key overrides the default command in the Docker image. It's used here to execute a script that initializes Kafka in KRaft mode and then runs Kafka:
    - It starts with a setup script.
    - `kafka-storage.sh` format is used to format the storage with a specific cluster ID and ignores if already formatted, indicating the initialization of KRaft mode storage.
    `Finally, it runs the main Kafka script.

#### 4. Environment Variables:

- These variables configure the Kafka broker to operate in KRaft mode, which means it functions without Zookeeper:
    - KAFKA_CFG_NODE_ID and KAFKA_CFG_BROKER_ID are set to 1, identifying the node and broker.
    - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS configures the Kafka controller's quorum voters, essential for the Raft consensus in KRaft mode.
    - Various listeners are set up for different purposes (external, internal, controller).
    - KAFKA_CFG_PROCESS_ROLES indicates that this broker also acts as a controller.

#### 5. Ports:

- Maps the Kafka broker’s ports to the host, allowing external access to these services.

#### 6. Networks:

- Connects the Kafka container to a Docker network named kafka-net, which is defined at the bottom of the file.

### B. Kafka UI Service

#### 1. Image Specification:

- image: provectuslabs/kafka-ui
- Specifies the Docker image for Kafka UI, a tool for managing Kafka clusters through a web interface.
Container Name:

#### 2. container_name: 
- kafka-ui

#### 3. Ports:

- Maps the port 8080 from the Kafka UI container to the same port on the host, allowing you to access the UI through the host’s IP.

#### 4. Restart Policy:

- restart: "always"
- Ensures that the Kafka UI container is always restarted if it stops.

#### 5. Environment Variables:

- Specifies the cluster name and the internal listener of the Kafka broker for the UI to connect to.

#### 6. Dependency:

- depends_on: - kafka
- Ensures that the Kafka container is started before the Kafka UI container.

#### 7. Networks:

- Connects the Kafka UI container to the same Docker network as the Kafka broker.

### C. Networks

- kafka-net:
    - Defines a Docker network with a bridge driver, allowing containers connected to this network to communicate internally.

## Why are we using bitnami/kafka image here?

The Bitnami images are designed to be easy to use and configure, especially in a Docker environment, and they come with certain conveniences and custom scripts.

## Takeaway 
Yes, this setup is using KRaft mode for Kafka, which is indicated by the KRaft-specific environment variables and the absence of any Zookeeper configuration. The setup is entirely focused on running Kafka with internal Raft consensus, which is a characteristic of KRaft mode.