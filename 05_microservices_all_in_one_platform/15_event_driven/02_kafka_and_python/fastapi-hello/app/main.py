from fastapi import FastAPI
from confluent_kafka import Producer, Consumer, KafkaError

###########
# KAFKA SETUP CONFIG
###########

# Kafka broker address and port - it's present in compose.yml
bootstrap_servers = 'kafka:9094' # for internal communication between containers we use the service name and port

# You have to manually create this topic using Kafka UI
topic = 'purchases'  

# Initialize the Kafka producer
producer = Producer({'bootstrap.servers': bootstrap_servers})

# A random group id for Consumer
group_id = 'my-consumer-group'  

# Initialize the Kafka consumer
consumer_config = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)
consumer.subscribe([topic])


app = FastAPI()

@app.get("/")
def read_root():
    """Simple API to return 'Hello World'."""
    return {"Hello": "World"}


@app.get("/produce")
def produce_message(user_id: str = "new_user", product: str = "skill"):
    """Endpoint to produce a message to the Kafka topic."""

    # Create a Message
    message = f"{user_id} bought {product}"

    # Producer sends the message to the Kafka topic
    producer.produce(topic, key=str(user_id), value=str(message))

    producer.flush()  # Ensure the message is sent

    return {"message": "Message sent to Kafka", "data": message}


@app.get("/consume")
def consume_message():
    """Endpoint to consume messages from the Kafka topic."""
    # Consume messages from the Kafka topic
    msg = consumer.poll(timeout=1.0)

    print("MSG \n\n", msg)

    # If no message is available, return a message
    if msg is None:
        return {"message": "No new messages"}

    # For any ERRORS return the error message
    elif msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            return {"message": "No more messages in topic"}
        else:
            return {"error": str(msg.error())}

    # Else Return the message
    else:
        return {
            "topic": msg.topic(),
            "key": msg.key().decode('utf-8') if msg.key() else None,
            "value": msg.value().decode('utf-8') if msg.value() else None
        }
