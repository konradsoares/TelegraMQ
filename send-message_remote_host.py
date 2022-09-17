#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('xx.xx.xx.xx'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Message from RabbitMQ Sender')
print(" [x] Sent 'Message from RabbitMQ Sender'")
connection.close()
