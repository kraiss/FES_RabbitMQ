#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='test_header', exchange_type='headers')

channel.queue_declare(queue='test_header_orange_rabbit')
channel.queue_bind(exchange='test_header', queue='test_header_orange_rabbit', routing_key='',
                   arguments={'animal': 'rabbit', 'color': 'orange', 'x-match': 'any'})

channel.queue_declare(queue='test_header_pink_panther')
channel.queue_bind(exchange='test_header', queue='test_header_pink_panther', routing_key='',
                   arguments={'animal': 'panther', 'color': 'pink', 'x-match': 'all'})

channel.basic_publish(exchange='test_header', routing_key='', body="Message rabbit",
                      properties=pika.BasicProperties(headers={'animal': 'rabbit'}))
channel.basic_publish(exchange='test_header', routing_key='', body="Message panther",
                      properties=pika.BasicProperties(headers={'animal': 'panther'}))
channel.basic_publish(exchange='test_header', routing_key='', body="Message pink panther",
                      properties=pika.BasicProperties(headers={'animal': 'panther', 'color': 'pink'}))

channel.close()
connection.close()
