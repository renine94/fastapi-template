from fastapi import APIRouter
from fastapi import Depends

from src.core.dependencies import get_api_key
from src.routers.v1 import question

router = APIRouter(prefix="/v1", tags=["v1"], dependencies=[Depends(get_api_key)])

__routers = [
    question.router,
]

for r in __routers:
    router.include_router(r)
