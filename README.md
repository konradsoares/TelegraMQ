# TelegraMQ
Simple RabbitMQ and Telegram Integration 

 What is Message Queueing?

The use of Message Queues provides a way for parts of the application to push messages to a queue asynchronously and ensure they are delivered to the correct destination. To implement message queuing, a message broker like RabbitMQ is a good option. The message broker works as a Middleware providing temporary message storage when the receiving service is busy or disconnected. 

The basic flow in a Message Queue is:

Producer - Generates and send the message to the Broker
Broker (Message Queue) - Receive and store the message, waiting to being consumed.
Consumers - One or more applications querying messages in one or more queues stored in the broker

![image](https://user-images.githubusercontent.com/52551615/190854332-ef00b071-8cc3-4f12-b1c9-c55bdefc4201.png)

Handling communication with brokers

A message broker acts as a middleman for the microservices, receiving messages from one application (producers) and handing them over to others (consumers) to do the job. For example; with RabbitMQ message broker, messages are not published directly to a queue. Instead, the producer sends a message to an exchange. The job of an exchange is to accept messages from the producer applications and route them to the correct message queues. The messages stay in the queue until the consumer handles them and removes them.

There are a couple of different message brokers to choose from. When choosing between brokers, you should try to nail down your requirements. RabbitMQ and Apache Kafka are two open-source message brokers.
You can read about the main difference between them in this comparison: "When to use RabbitMQ or Apache Kafka" https://www.cloudamqp.com/blog/when-to-use-rabbitmq-or-apache-kafka.html. 
