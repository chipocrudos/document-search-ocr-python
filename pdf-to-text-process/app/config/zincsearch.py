from .configuration import zincConfig
from repository.zincsearch import ZincSearch
import requests

zincsearch = ZincSearch(zincConfig, requests.session())

