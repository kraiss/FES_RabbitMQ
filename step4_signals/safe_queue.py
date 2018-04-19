#!/usr/bin/env python
import pika


class Step4Consumer:
    def start(self):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue='safe_hello')
        self._channel.basic_consume(queue='safe_hello', no_ack=True, consumer_callback=self.consume)
        self._channel.add_on_cancel_callback(self.on_cancel)
        self._channel.start_consuming()

    def on_cancel(self, method_frame):
        self._channel.close()
        self._connection.close()
        self.start()

    def consume(self, channel, envelope, props, body):
        print("Consumer receives : %s" % body)


Step4Consumer().start()

