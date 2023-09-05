"""EXCEPTION HANDLER
Middleware to handle exception or pass it.
"""

from fastapi import Request

from app.utils.custom_exception import *

__all__ = ("request_handler",)


async def request_handler(request: Request, call_next):
    """Middleware used to process each request on FastAPI, to provide error handling (convert exceptions to responses)."""
    try:
        return await call_next(request)

    except Exception as ex:
        if isinstance(ex, BaseAPIException):
            return ex.response()

        # Re-raising other exceptions will return internal error 500 to the client
        raise ex
