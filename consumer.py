import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=8081))
channel = connection.channel()

channel.queue_declare(queue='tasks', durable=True, arguments={'x-queue-type': 'quorum'})

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

channel.basic_consume(queue='tasks',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()