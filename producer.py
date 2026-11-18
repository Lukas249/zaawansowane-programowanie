import random

import pika

connection = pika.Connection(pika.ConnectionParameters('localhost', port=8081))
channel = connection.channel()

channel.queue_declare(queue='tasks', durable=True, arguments={'x-queue-type': 'quorum'})

body = f"Task{random.randint(0, 1000)}"

channel.basic_publish(exchange='',
                      routing_key='tasks',
                      body=body)
print(f" [x] Sent {body}")

connection.close()