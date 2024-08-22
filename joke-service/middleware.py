from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from logger import log_request


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        account_status = request.headers.get("Authorization", "UNAUTHORIZED")
        response: Response = await call_next(request)
        log_request(request, response, account_status)
        return response
