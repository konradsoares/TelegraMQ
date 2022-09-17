#!/usr/bin/env python
import pika
import requests

credentials = pika.PlainCredentials('rabit_admin', '123456789')
# Note: sending a short heartbeat to prove that heartbeats are still
# sent even though the worker simulates long-running work
parameters =  pika.ConnectionParameters('78.111.84.97', credentials=credentials, heartbeat=5)
connection = pika.BlockingConnection(parameters)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    requests.post('https://api.telegram.org/bot5724697155:AAE8SMp_Nfy9A8e5sp1fNp4rPWdx3Aw9gWA/sendMessage?chat_id=1278083505&text='+body)
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
