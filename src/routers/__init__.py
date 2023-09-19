from fastapi import APIRouter

from src.core import settings
from src.dtos.responses.base import MessageResponse
from src.dtos.responses.base import VersionResponse
from src.routers import v1

router = APIRouter()

__routers = [
    v1.router,
]

for r in __routers:
    router.include_router(r)


@router.get("/", response_model=VersionResponse)
async def index():
    return {"version": settings.VERSION}


@router.get("/health", response_model=MessageResponse)
async def health_check():
    return {"message": "OK"}
