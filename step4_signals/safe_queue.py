#!/usr/bin/env python
import pika


class Step4Consumer:
    def start(self):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = self._connection.channel()
        channel.queue_declare(queue='safe_hello')
        channel.basic_consume(queue='safe_hello', no_ack=True, consumer_callback=self.consume)
        channel.add_on_cancel_callback(self.on_cancel)
        channel.start_consuming()

    def on_cancel(self, method_frame):
        self._connection.close()
        self.start()

    def consume(self, channel, envelope, props, body):
        print("Consumer receives : %s" % body)


Step4Consumer().start()

