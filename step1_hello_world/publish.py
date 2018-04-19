#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
for i in range(0, 10, 1):
    message = 'Message %s' % i;
    print("basic_publish : %s" % message)
    channel.basic_publish(exchange='', routing_key='hello', body=message)
channel.close()
connection.close()
