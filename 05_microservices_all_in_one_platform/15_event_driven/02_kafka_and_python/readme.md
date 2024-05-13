## Getting Started with Kafka in Python

In this helloworld we will create a single FastAPI microservice that can produce messages/events to a topic and then consume them using another API endpoint.

The compose file is extended from step01 to add microservice(fastapi-hello) details.

Note: For Kafka in Python we are using confluent-kafka package. 

Follow these steps:

1. Clone repo and open this step in VS Code 

2. Run `docker compose up --build`

3. Open localhost:8080 (kafka-ui) and create a new topic name: `purchases`. Refer to last step readme to see how topics are created.

4. Now open localhost:8000/docs and 

    - Call /produce endpoint
        - This will write a message in our topic that you can verify from kafka ui.

    - Call /consume endpoint
        - This will consume that message
        - calling it again shows no more events are present to consume

Now visit kafka ui again to see update metrics.

After this hello world we will learn how to create Topics with FastAPI and then setup complete microservice example

https://github.com/confluentinc/confluent-kafka-python

More Learning Resources:

https://developer.confluent.io/get-started/python/#create-project

https://towardsdatascience.com/3-libraries-you-should-know-to-master-apache-kafka-in-python-c95fdf8700f2

https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html

https://stackoverflow.com/questions/73049329/python-kafka-consumer-library-that-supports-scalability-and-recoverability

https://www.confluent.io/en-gb/blog/event-driven-microservices-with-python-and-kafka/
