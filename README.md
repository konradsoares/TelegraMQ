# TelegraMQ
Simple RabbitMQ and Telegram Integration with Python

<h1><b>What is Message Queueing?</b></h1>

The use of Message Queues provides a way for parts of the application to push messages to a queue asynchronously and ensure they are delivered to the correct destination. To implement message queuing, a message broker like RabbitMQ is a good option. The message broker works as a Middleware providing temporary message storage when the receiving service is busy or disconnected. 

<b>The basic flow in a Message Queue is:</b>

<p><b>Producer</b> - Generates and send the message to the Broker
<p><b>Broker</b> (Message Queue) - Receive and store the message, waiting to being consumed.
<p><b>Consumers</b> - One or more applications querying messages in one or more queues stored in the broker

![image](https://user-images.githubusercontent.com/52551615/190854332-ef00b071-8cc3-4f12-b1c9-c55bdefc4201.png)

<h1><b>Handling communication with brokers</b></h1>

A message broker acts as a middleman for the microservices, receiving messages from one application (producers) and handing them over to others (consumers) to do the job. For example; with RabbitMQ message broker, messages are not published directly to a queue. Instead, the producer sends a message to an exchange. The job of an exchange is to accept messages from the producer applications and route them to the correct message queues. The messages stay in the queue until the consumer handles them and removes them.

There are a couple of different message brokers to choose from. When choosing between brokers, you should try to nail down your requirements. RabbitMQ and Apache Kafka are two open-source message brokers.
You can read about the main difference between them in this comparison: "When to use RabbitMQ or Apache Kafka" https://www.cloudamqp.com/blog/when-to-use-rabbitmq-or-apache-kafka.html. 

<b>RabbitMQ</b> enables asynchronous processing, meaning that it allows you to put a message in a queue without processing it immediately. 

<b>RabbitMQ</b> is therefore ideal for long-running tasks or blocking tasks, allowing web servers to respond quickly to requests instead of being forced to perform computationally intensive tasks on the spot. RabbitMQ simply stores messages and passes them to consumers when ready.

<li><b>RabbitMQ</b> is a reliable open source message broker. It has been on the market since 2007 and became a part of Pivotal software 2013. It's continuously updated and improved upon. RabbitMQ has a strong community and highly active core team that produce additional features, improvements and handy plugins. The license of RabbitMQ has never changed (Nov 2019).

<li><b>RabbitMQ</b> supports several standardized protocols such as AMQP, MQTT, STOMP, etc. where it natively implements AMQP 0.9.1. The ability of RabbitMQ to support different standardized message protocols means that it can be used in many different scenarios and it allows you to replace your RabbitMQ broker with any AMQP based broker.

<li><b>RabbitMQ</b> is used by a large number of companies within various industries and is used and trusted by large companies (Zalando, WeWork, Wunderlist, Bloomberg, and more). All relying on a microservice based architecture.

<li><b>RabbitMQ</b> is user-friendly, and by following these RabbitMQ best practices, it is easy to tweak the configurations to suit the intended purpose. RabbitMQ is written in Erlang and is the world’s most deployed open-source message broker, meaning that it’s a well-tested, robust broker.

<li>The <b>RabbitMQ</b> broker is scalable and flexible. Your team only needs to maintain the producers and the consumers sending and receiveing messages to/from the queue. Under heavy load, if the queue grows larger, the standard reaction is to add more consumers and parallelize the work. This is a simple and effective method of scaling.
 
 
 
<h1><b>Benefits of Message Queues</b></h1>

In modern cloud architecture, applications are decoupled into smaller, independent building blocks that are easier to develop, deploy and maintain. Message queues provide communication and coordination for these distributed applications.

Message queues can significantly simplify coding of decoupled applications, while improving performance, reliability and scalability. You can also combine message queues with Pub/Sub messaging in a fanout design pattern.
 
 
<li><b>Better Performance</b>

Message queues enable asynchronous communication, which means that the endpoints that are producing and consuming messages interact with the queue, not each other. Producers can add requests to the queue without waiting for them to be processed. Consumers process messages only when they are available. No component in the system is ever stalled waiting for another, optimizing data flow.


<li><b>Increased Reliability</b>

Queues make your data persistent, and reduce the errors that happen when different parts of your system go offline. By separating different components with message queues, you create more fault tolerance. If one part of the system is ever unreachable, the other can still continue to interact with the queue. The queue itself can also be mirrored for even more availability.


<li><b>Granular Scalability</b>

Message queues make it possible to scale precisely where you need to. When workloads peak, multiple instances of your application can all add requests to the queue without risk of collision. As your queues get longer with these incoming requests, you can distribute the workload across a fleet of consumers. Producers, consumers and the queue itself can all grow and shrink on demand.
 

<li><b>Simplifed Decoupling</b>

Message queues remove dependencies between components and significantly simplify the coding of decoupled applications. Software components aren’t weighed down with communications code and can instead be designed to perform a discrete business function.

Message queues are an elegantly simple way to decouple distributed systems, whether you're using monolithic applications, microservices or serverless architectures.

 
Now that you know more about Message Queues let's do a simple example using Python, Python Pika, RabbitMQ and Telegram.

<h1><b>In this POC we gonna follow the steps bellow:</b></h1> 
 
<p><li> Create 2 Ubuntu 20.04 VPcs
<p><li> Install Python, Pika and RabbitMQ in the Server 2, then create our receiver for queue the message then send to the telegram bot.
<p><li> Install Python and Pika in the Server 1 (Sender), then create our application for sending message to the queue.
 
<p>In the fisrt step we gonna use server 2 as a Broker and Consumer, sending our message locally via localhost to our Telegram Bot.
<p>In the second step, we gonna allow our guest user for sending our message remotely to our Telegram Bot.
 
 Let's start updating our Ubuntu OS.
 
 root@MQBroker:~# sudo apt update && sudo apt upgrade
 <br>![image](https://user-images.githubusercontent.com/52551615/190864431-7eb35e95-47f1-4a49-9dd8-f1eaa16cf945.png)
 <br>
 Our installation already have python3.8 So let's install python-pika.
 <br>![image](https://user-images.githubusercontent.com/52551615/190864865-adc66f71-07ce-47c6-89cd-81cf92d0cb8c.png)
<br>
 Upload rabbitmq.conf, rabbitmq-install.sh, receive-message.py and send-message_localhost.py to your server.
 <br>
 Let's install RabbitMQ now. Just execute the bash script rabbitmq-install.sh.
 
![image](https://user-images.githubusercontent.com/52551615/190865190-9146f990-8ecb-4578-b659-f5f641b9623c.png)
<br>root@MQBroker:~# sh rabbitmq-install.sh
 <p>After the script finishes, our RabbitMQ Server is already installed and running.</p>
 <p>You can check running the comand:</p>
 <p>root@MQBroker:~# sudo systemctl status rabbitmq-server</p>

![image](https://user-images.githubusercontent.com/52551615/190865777-1703056a-996e-4de7-9d61-5c233d74816d.png)
 
 
 If you run receive-message.py now, you gonna start our consumer, and will connect to our queue waiting for some message.
 
 ![image](https://user-images.githubusercontent.com/52551615/190865889-a548c876-7479-42f1-b859-4bd1ef0ddf3d.png)
 
 You can test if is working, opening another ssh session then running send-message_localhost.py.
 
 ![image](https://user-images.githubusercontent.com/52551615/190866585-c4f8e7ff-dc30-459c-b2bc-77d05132abeb.png)
 
 You can also stop the receiver application and send some messages to the broker.
 
 ![image](https://user-images.githubusercontent.com/52551615/190867699-80b048c2-d65a-4b71-8b99-0718a164df1f.png)

 Here we've sent 3 messages with the receiver down.
 
 Now if you run again the receiver, it will print all the 3 messages stored in the queue.
 
 ![image](https://user-images.githubusercontent.com/52551615/190867804-f1edb44a-271e-49d8-93e3-1b94f93a9076.png)

 
 Ok, we have our Broker working locally, but doesn't make sense right? We want it receiving messages from one application in another server and for this, we need to create the rabbitmq.conf setting some permission for our user guest connecting the broker remotely.
 
 Let's move to the next step installing Python and Pika in the server MQSender.
 You can repeat the same steps we followed for the Broker, we just don't need to install RabbitMQ in the MQSender.
 
 ![image](https://user-images.githubusercontent.com/52551615/190872493-041f1e72-519c-47b8-a91d-e780bfe32811.png)

 ![image](https://user-images.githubusercontent.com/52551615/190872510-75a10534-41d7-4b5c-9d4d-eda2a70270f4.png)

 Now you can copy the python script send-message_remote_host.py to your MQSender server and put your MQBroker Server IP in my case is 78.111.85.11.
 
 ![image](https://user-images.githubusercontent.com/52551615/190872579-90262232-10d0-4bbc-95d1-f78ece63adc8.png)

 If you run the script now you'll get an ERROR.
 pika.exceptions.ProbableAuthenticationError: (403, 'ACCESS_REFUSED - Login was refused using authentication mechanism PLAIN. For details see the broker logfile.')
 ![image](https://user-images.githubusercontent.com/52551615/190872626-b6ddef0a-7b30-4d89-9385-c2b9041946e7.png)

 This is because we don't have the RabbitMQ config file with the Access Control configuration, permiting guest user to connect outside the loopback.
 
 ![image](https://user-images.githubusercontent.com/52551615/190872872-0a9fbe76-7fff-4572-92a0-5628cc7102ae.png)

 You can upload the rabbitmq.conf here to your MQBroker server in the directory /etc/rabbitmq
 
 ![image](https://user-images.githubusercontent.com/52551615/190872983-51310496-fabf-4cc4-b93c-0859faaac268.png)

 
 
