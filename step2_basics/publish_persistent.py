#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='durable_hello', durable=True)

persistent = pika.BasicProperties(delivery_mode = 2,)
for i in range(0, 10, 1):
    message = 'Message %s' % i
    print("basic_publish : %s" % message)
    channel.basic_publish(exchange='', routing_key='durable_hello', body=message, properties=persistent)

channel.close()
connection.close()
