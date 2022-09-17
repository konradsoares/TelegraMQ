#!/usr/bin/env python
import pika
import requests

credentials = pika.PlainCredentials('guest', 'guest')
# Note: sending a short heartbeat to prove that heartbeats are still
# sent even though the worker simulates long-running work
parameters =  pika.ConnectionParameters('localhost', credentials=credentials, heartbeat=5)
connection = pika.BlockingConnection(parameters)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ## If you get the characther b (byte) in your message you can use the line bellow to convert repr to string.
    ##print(" [x] Received " + body.decode('utf-8'))
    #requests.post('https://api.telegram.org/bot<YOUR TELEGRAM BOT TOKEN>/sendMessage?chat_id=<your_telegram_chatID>&text='+body.decode('utf-8'))
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
