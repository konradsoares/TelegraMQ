#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('78.111.84.97'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Message from RabbitMQ')
connection.close()
