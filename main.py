"""main file for  FastAPI"""
from app import logger
from fastapi.responses import RedirectResponse
from fastapi import FastAPI

from app.version import __version__

from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes.user import router as user_router
from app.db.base import db

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


@app.on_event("startup")
async def startup():
    """Initialize Database."""
    await db.init()
    # await db.create_all()


logger.info("FastAPI server started!!!")


@app.get("/")
def get_root():
    """
    The API root, redirects to docs.

    :returns: Redirection to the redoc page.
    """
    return RedirectResponse(url="docs/")


app.include_router(user_router)
