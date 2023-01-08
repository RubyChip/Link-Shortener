import logging
from fastapi import FastAPI

from app.api.api_v1.router import api_router
from app.configs.base import settings

logging.basicConfig(level=logging.WARNING, format="%(asctime)s %(levelname)s %(message)s")

app = FastAPI(title=settings.PROJECT_NAME)


app.include_router(api_router, prefix=settings.API_V1)
