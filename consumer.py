import pika

params = pika.URLParameters('amqps://vaihkxgq:WNZrLPL6jg44KIhv0QEoEDk_ButDDPmb@cow.rmq2.cloudamqp.com/vaihkxgq')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Receiving in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
