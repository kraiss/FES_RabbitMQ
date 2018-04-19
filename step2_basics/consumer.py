#!/usr/bin/env python
import pika

class Step2Consumer:
    def __init__(self, id):
        self.id = id

    def consume(self, channel, envelope, props, body):
        print("Consumer %s receives : %s" % (self.id, body))
        channel.basic_ack(delivery_tag=envelope.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_qos(prefetch_count=1)

consumer = Step2Consumer('1')
channel.basic_consume(queue='hello', consumer_callback=consumer.consume)

consumer = Step2Consumer('2')
channel.basic_consume(queue='hello', consumer_callback=consumer.consume)

print("Start consuming...")
channel.start_consuming()
