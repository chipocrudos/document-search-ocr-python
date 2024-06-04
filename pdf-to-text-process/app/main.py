from types import FunctionType
from typing import Any, Callable, List, Type
from config.bucket import s3_bucket
from config.rabbitmq import get_connection_listener
from config.zincsearch import zincsearch
from config.logger import logger
from model.message import Message
from model.document import Document, ProtoDocument
from tools.filedownload import filedownload
from tools.covertpdf import covert_pdf
from repository.repository import ProtoRepository


def callback(
        download: Callable[[str], tuple[str, str]],
        convert: Callable[[str, str, str, List[str], str, Type[ProtoDocument]], List[ProtoDocument]],
        repository: ProtoRepository
) -> FunctionType:
    def call(ch: Any, method: Any, properties: Any, body: Any):
        try:
            message: Message = Message.create_message(body)
            logger.info(f" [x] Received {message}")
            folder, filename = download(message.path)
            logger.info(f" [x] File downloaded to {folder}/{filename}")
            
            documents = convert(
                folder,
                filename,
                message.index,
                message.tags,
                message.path,
                Document
            )

            logger.info(f" [x] Saving documents to ZincSearch...")
            repository.create_bulk_documents(message.index, documents)
            logger.info(f" [x] Documents saved to ZincSearch")

            ch.basic_ack(delivery_tag=method.delivery_tag)
            logger.info(f" [x] Acknowledged message {message}")

        except ValueError as e:
            ch.basic_ack(delivery_tag=method.delivery_tag)
            logger.error(f" [x] Error: {e}")

    return call


if __name__ == '__main__':
    bucket = s3_bucket()
    download = filedownload(bucket)
    convert = covert_pdf()
    channel = get_connection_listener(
        callback(download, convert, zincsearch)
    )
    logger.info(' [*] Waiting for messages. To exit press CTRL+C')

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        logger.warning(' [*] Stopped consuming messages')
        channel.close()

    