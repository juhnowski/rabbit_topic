import pika
import sys

if __name__ == '__main__':

    topic_name = 'topic_golive-renderer'
    routing_key = 'golive-renderer.command'
    message = '50051 50041 rtmp://gpu3.view.me/live/test890'

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange=topic_name, exchange_type='topic')

    channel.basic_publish(
        exchange=topic_name, routing_key=routing_key, body=message)
    print(" [x] Sent %r:%r" % (routing_key, message))
    connection.close()