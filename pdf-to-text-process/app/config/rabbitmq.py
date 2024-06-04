from types import FunctionType
from typing import Any
from .configuration import rabbitmqConfig
import pika


def get_connection_listener(callback: FunctionType) -> Any:
    connection_params: pika.ConnectionParameters = pika.ConnectionParameters(
            host=rabbitmqConfig.RABBITMQ_HOST,
        )
    connection = pika.BlockingConnection(connection_params)

    channel = connection.channel()
    channel.queue_declare(queue=rabbitmqConfig.RABBITMQ_QUEUE)

    channel.basic_qos(prefetch_count=rabbitmqConfig.RABBITMQ_PREFETCH_COUNT)

    channel.basic_consume(
        queue=rabbitmqConfig.RABBITMQ_QUEUE,
        on_message_callback=callback, auto_ack=False
    )

    return channel
