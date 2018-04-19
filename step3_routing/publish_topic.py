#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='test_topic', exchange_type='topic')

channel.queue_declare(queue='test_topic_orange')
channel.queue_bind(exchange='test_topic', queue='test_topic_orange', routing_key='*.orange.*')

channel.queue_declare(queue='test_topic_rabbit')
channel.queue_bind(exchange='test_topic', queue='test_topic_rabbit', routing_key='*.*.rabbit')

channel.queue_declare(queue='test_topic_lazy')
channel.queue_bind(exchange='test_topic', queue='test_topic_lazy', routing_key='lazy.#')

channel.basic_publish(exchange='test_topic', routing_key='quick.orange.fox', body="Message quick.orange.fox")
channel.basic_publish(exchange='test_topic', routing_key='quick.orange.rabbit', body="Message quick.pink.rabbit")
channel.basic_publish(exchange='test_topic', routing_key='lazy.orange.elephant', body="Message lazy.pink.elephant")
channel.basic_publish(exchange='test_topic', routing_key='lazy.orange.elephant', body="Message lazy.orange.elephant")
channel.basic_publish(exchange='test_topic', routing_key='quick.orange.rabbit', body="Message quick.orange.rabbit")
channel.basic_publish(exchange='test_topic', routing_key='lazy.pink.rabbit.male', body="Message lazy.pink.rabbit.male")
channel.basic_publish(exchange='test_topic', routing_key='quick.pink.rabbit.male', body="Message quick.pink.rabbit.male")

channel.close()
connection.close()
