#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
while True:
    message = channel.basic_get(queue='step1', no_ack=True)
    if message[0] is not None:
        print("basic_get : %s" % message[2])
    else: break
channel.close()
connection.close()
