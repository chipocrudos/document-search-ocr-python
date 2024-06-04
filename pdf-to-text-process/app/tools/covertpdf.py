from types import FunctionType
from typing import TypeVar, List
from pdf2image import convert_from_path
from model.document import ProtoDocument
from config.configuration import appConfig
from config.logger import logger
from PIL.Image import Image
from time import time
from shutil import rmtree
import pytesseract
import asyncio


T = TypeVar('T')


# Configura Tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


async def image_to_string(i: int, page: Image) -> tuple[int, str]:
    logger.info(f"initiandig text from page {i}")
    text :str = await asyncio.get_running_loop().run_in_executor(
        None, pytesseract.image_to_string, page, 'spa'
    )
    logger.info(f"Extracted text from page {i}")
    return i, text


async def limit_concurrent(sem: asyncio.Semaphore, i: int, page: Image ) -> tuple[int, str]:
    async with sem:
        return await image_to_string(i, page)


# Función para procesar un PDF
def covert_pdf() -> FunctionType:
    loop = asyncio.get_event_loop()
    sem = asyncio.Semaphore(appConfig.ASYNCRONOUS_SEMAPHORE)

    def process_pdf(
            pdf_path: str,  pdf_file: str,
            index: str, tags: List[str], path: str, md: ProtoDocument
        ) -> List[ProtoDocument]:

        start_time = time()

        full_path = f"{pdf_path}/{pdf_file}"
        logger.info(f"Processing {full_path}...")
        pages = convert_from_path(full_path)
        logger.info(f"Extrating images ...")

        async def runner() -> List[tuple[int, str]]:
            logger.info("Creating async tasks...")
            tasks = []
            for i, page in enumerate(pages):
                tasks.append(limit_concurrent(sem, i+1, page))

            results: List[tuple[int, str]] = await asyncio.gather(*tasks)
            return results
        
        logger.info("Running async tasks...")
        pages_text = loop.run_until_complete(runner())
        document: List[ProtoDocument] = []
        for i, p in pages_text:
            document.append(
                md.create_document(index=index, tags=tags, path=path, page=i, content=p)
            )

        logger.info(f"Processed {full_path}: total pages {i}")
        logger.info(f"Eliminando arhcivo {full_path}")
        # Elimina el archivo PDF
        rmtree(pdf_path)

        logger.info(f"Tiempo de ejecución: {time() - start_time}")

        return document

    return process_pdf

