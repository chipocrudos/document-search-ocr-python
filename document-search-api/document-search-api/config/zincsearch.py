from .configuration import zincConfig
from repository.zincsearch import ZincSearch
import httpx


async def get_search():
    yield ZincSearch(zincConfig, httpx.Client())

