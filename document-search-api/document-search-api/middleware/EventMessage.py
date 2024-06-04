from typing import Any
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp



class EventMiddleware(BaseHTTPMiddleware):

    def __init__(self, app: ASGIApp, path: str, brocker: Any) -> None:
        super().__init__(app)
        self.path = path
        self.brocker = brocker
        

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        response = await call_next(request)
        # Aquí es donde puedes ejecutar tu código después de que se ha completado la solicitud.
        if request.url.path.startswith(self.path):
            print("After request")
            print(request.url.path)
            await self.brocker().basic_publish(exchange='', routing_key="d", body="Hello World")
        
        return response
