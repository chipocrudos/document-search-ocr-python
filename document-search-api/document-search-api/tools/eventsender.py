from typing import Any
from fastapi import Depends
from config.rabbitmq import get_connection, rabbitmqConfig


async def send_message(connection: Any = Depends(get_connection)):
    channel = connection.channel()
    channel.queue_declare(queue=rabbitmqConfig.RABBITMQ_QUEUE)

    def send(message: str):
        channel.basic_publish(exchange='', routing_key=rabbitmqConfig.RABBITMQ_QUEUE, body=message)
        print(f" [x] Sent '{message}'")
        channel.close()

    return send



# def send_message(queue, message):
#     channel = get_channel()
#     channel.queue_declare(queue=queue)
#     channel.basic_publish(exchange='', routing_key=queue, body=message)
#     print(f" [x] Sent '{message}'")
#     channel.close()

# def receive_message(queue):
#     channel = get_channel()
#     channel.queue_declare(queue=queue)
#     method_frame, header_frame, body = channel.basic_get(queue=queue)
#     if method_frame:
#         print(f" [x] Received '{body}'")
#         channel.basic_ack(delivery_tag=method_frame.delivery_tag)
#     else:
#         print('No message returned')
#     channel.close()

