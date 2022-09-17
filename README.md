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

RabbitMQ enables asynchronous processing, meaning that it allows you to put a message in a queue without processing it immediately. RabbitMQ is therefore ideal for long-running tasks or blocking tasks, allowing web servers to respond quickly to requests instead of being forced to perform computationally intensive tasks on the spot. RabbitMQ simply stores messages and passes them to consumers when ready.

    RabbitMQ is a reliable open source message broker. It has been on the market since 2007 and became a part of Pivotal software 2013. It's continuously updated and improved upon. RabbitMQ has a strong community and highly active core team that produce additional features, improvements and handy plugins. The license of RabbitMQ has never changed (Nov 2019).
    RabbitMQ supports several standardized protocols such as AMQP, MQTT, STOMP, etc. where it natively implements AMQP 0.9.1. The ability of RabbitMQ to support different standardized message protocols means that it can be used in many different scenarios and it allows you to replace your RabbitMQ broker with any AMQP based broker.
    RabbitMQ is used by a large number of companies within various industries and is used and trusted by large companies (Zalando, WeWork, Wunderlist, Bloomberg, and more). All relying on a microservice based architecture.
    RabbitMQ is user-friendly, and by following these RabbitMQ best practices, it is easy to tweak the configurations to suit the intended purpose. RabbitMQ is written in Erlang and is the world’s most deployed open-source message broker, meaning that it’s a well-tested, robust broker.
    The RabbitMQ broker is scalable and flexible. Your team only needs to maintain the producers and the consumers sending and receiveing messages to/from the queue. Under heavy load, if the queue grows larger, the standard reaction is to add more consumers and parallelize the work. This is a simple and effective method of scaling.
