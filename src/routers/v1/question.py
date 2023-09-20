from fastapi import APIRouter

from src.dtos.requests.question import QuestionCreateRequest
from src.services.question import QuestionService

router = APIRouter(prefix="/question")


@router.post("", status_code=201)
async def create_question(request: QuestionCreateRequest):
    script_parts = QuestionService.split_script(**request.model_dump())
    questions = await QuestionService.bulk_create_from_openai(script_parts)
    return questions
