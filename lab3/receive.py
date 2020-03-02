#!/usr/bin/python

# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# RECEIVE

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='pingpong')

def callback(ch, method, properties, body):
    if(body == 'ping'):
        print("Received:", body)
        channel.basic_publish(exchange='',
                           routing_key='pingpong',
                           body='pong')

channel.basic_consume(queue='pingpong',
                      auto_ack=True,
                      on_message_callback=callback)

print('Waiting for messages...')
channel.start_consuming()
