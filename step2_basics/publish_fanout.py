#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='test_fanout', exchange_type='fanout')
channel.queue_declare(queue='fanout1')
channel.queue_bind(exchange='test_fanout', queue='fanout1')
channel.queue_declare(queue='fanout2')
channel.queue_bind(exchange='test_fanout', queue='fanout2')
for i in range(0, 10, 1):
    message = 'Message %s' % i
    print("basic_publish : %s" % message)
    channel.basic_publish(exchange='test_fanout', routing_key='', body=message)
channel.close()
connection.close()
