from typing import Any
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.document import DocumentResponse
from models.search import DocumentSearch
from tools.uploadfile import upload_file
from tools.download import upload_from_url
from tools.eventsender import send_message
from config.configuration import appConfig
from config.zincsearch import get_search
from repository.repository import ProtoRepository


app = FastAPI(title="Document Search API", version="0.0.1")


app.add_middleware(
    CORSMiddleware,
    allow_origins=appConfig.CORS_DOMAINS,
    allow_credentials=True,
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/api/healthcheck")
async def main():
    return {"message": "Is a live"}


@app.post("/api/documents/file/", response_model=DocumentResponse)
async def create_document_from_file(
    document: DocumentResponse = Depends(upload_file)
):
    return document


@app.post("/api/documents/path/")
async def create_document_from_url(
    document: DocumentResponse,
    sendmessage: Any = Depends(send_message)
):
    sendmessage(document.model_dump_json())
    
    return document


@app.post("/api/documents/download/", response_model=DocumentResponse)
async def create_document_from_download(
    document: DocumentResponse = Depends(upload_from_url),
    sendmessage: Any = Depends(send_message)
):
    sendmessage(document.model_dump_json())
    return document


@app.get("/api/search/")
async def index_list(
    search: ProtoRepository = Depends(get_search)
):
    return search.get_all_index()


@app.get("/api/search/{index}")
async def index_tags_list(
    index: str,
    search: ProtoRepository = Depends(get_search)
):
    
    return search.get_index_tags(index)


@app.post("/api/search/{index}")
async def index_search(
    index: str,
    filter: DocumentSearch,
    search: ProtoRepository = Depends(get_search)
):
    
    return search.get_search(index, filter.tags, filter.content)
