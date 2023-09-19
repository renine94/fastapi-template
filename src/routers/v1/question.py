from fastapi import APIRouter

from src.dtos.requests.question import QuestionCreateRequest
from src.services.question import QuestionService

router = APIRouter(prefix="/question")


@router.post("", status_code=201)
async def create_question(request: QuestionCreateRequest):
    return QuestionService.bulk_create(request)
