#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='test_direct', exchange_type='direct')

channel.queue_declare(queue='test_direct_orange')
channel.queue_bind(exchange='test_direct', queue='test_direct_orange', routing_key='orange')

channel.queue_declare(queue='test_direct_black')
channel.queue_bind(exchange='test_direct', queue='test_direct_black', routing_key='black')

channel.queue_declare(queue='test_direct_black2')
channel.queue_bind(exchange='test_direct', queue='test_direct_black2', routing_key='black')

channel.basic_publish(exchange='test_direct', routing_key='orange', body="Message orange")
channel.basic_publish(exchange='test_direct', routing_key='black', body="Message black")
channel.basic_publish(exchange='test_direct', routing_key='green', body="Message green")

channel.close()
connection.close()
