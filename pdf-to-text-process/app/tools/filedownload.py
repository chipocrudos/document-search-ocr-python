import tempfile
from types import FunctionType
from typing import Callable


def filedownload(bucket: FunctionType) -> Callable[[str], tuple[str, str]]:

    def download(file: str) -> tuple[str, str] :
        folder = tempfile.mkdtemp(prefix='docs_')
        filename: str = bucket(file, folder)
        
        return folder, filename
        
    return download
