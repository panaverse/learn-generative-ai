# 03 Protobuf Kafka Messaging

### 1. Review Protobuf and how it works in python

https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/14_docker/08_kafka/protobuf

### 2. Build and Start Docker Containers

`docker compose up --build`

### 3. Installing Protobuf Compiler in Container

- In `todo` Dockerfile.dev we have added installation command at line-11 for `protobuf-compiler` package. 
- We will use the protoc compiler to generate the Python code from the .proto files.  i.e: protoc --python_out=. todo.proto


### 4. Install Protobuf Python Package in `todo` microservice

- We need a protobuf package in Python.
- We have already installed it here. See the todo pyproject.toml.
- For new projects we will install it in our microservice using Poetry: `poetry add protobuf`.

### 5. Generate python code for ProtoSchema in `todo.proto` (todo/app/todo.proto).

```
docker exec -it <cont-name> /bin/bash

cd app

protoc --python_out=. todo.proto
```

It will generate `todo_pb2.py` file.

### 6. Now review how the generated python code is used in `main.py` with producers and consumers.

- Before Producing Serialize using Generated Class
```
    todo_protbuf = todo_pb2.Todo(id=todo.id, content=todo.content)
    print(f"Todo Protobuf: {todo_protbuf}")

    # Serialize the message to a byte string
    serialized_todo = todo_protbuf.SerializeToString()
    print(f"Serialized data: {serialized_todo}")
    
    # Produce message
    await producer.send_and_wait("todos2", serialized_todo)
```

- Deserialize In Consumer

```
async def consume_messages(topic, bootstrap_servers):
    # Create a consumer instance.
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        group_id="my-group",
        auto_offset_reset='earliest'
    )

    # Start the consumer.
    await consumer.start()
    try:
        # Continuously listen for messages.
        async for message in consumer:
            print(f"\n\n Consumer Raw message Vaue: {message.value}")

            new_todo = todo_pb2.Todo()
            new_todo.ParseFromString(message.value)
            print(f"\n\n Consumer Deserialized data: {new_todo}")
        # Here you can add code to process each message.
        # Example: parse the message, store it in a database, etc.
    finally:
        # Ensure to close the consumer when done.
        await consumer.stop()
```

Now we are producing and consuming messages that are serialized using Protobuf. Next, we will learn about Schema Registry.