"""APP
FastAPI app definition, initialization and definition of routes
"""

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

from app import logger
from app.api.router import router
from app.core.config import settings
from app.db.base import db
from app.middlewares.exception_handler import request_handler
from app.version import __version__

app = FastAPI(
    title="FastApi Service",
    description="Explore the comprehensive OpenAPI documentation for the iNotebook project's backend. This repository provides detailed insights into the APIs, endpoints, request and response formats, authentication methods, and usage examples, ensuring smooth integration and interaction with the iNotebook application's core functionalities.",
    version=__version__,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

app.middleware("http")(request_handler)


@app.on_event("startup")
async def startup():
    """Initialize Database."""
    logger.info("FastAPI server started!!!")
    logger.info("Connecting Mongodb")
    await db.init()
    logger.info("Mogodb Connnected!!!")


@app.get("/")
def get_root():
    """
    The API root, redirects to docs.

    :returns: Redirection to the redoc page.
    """
    return RedirectResponse(url="docs/")


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_config="logger.yaml",
    )
