#!/usr/bin/python

# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# SEND

import pika
from time import sleep

# Connect to localhost, since our broker is on the same machine
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue, or else the messages are just dropped
channel.queue_declare(queue='pingpong')

def callback(ch, method, properties, body):
    if(body == 'pong'):
        print("Received:", body)

channel.basic_consume(queue='pingpong',
                      auto_ack=True,
                      on_message_callback=callback)


# Send a message (body) to the right queue (pingpong)
channel.basic_publish(exchange='',
                      routing_key='pingpong',
                      body='ping')
print("Sent ping...")




channel.start_consuming()

try:
    while(True):
        print("Waiting for pong..")
        sleep(1)
except:
    print("Exiting..")

