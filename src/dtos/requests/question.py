from pydantic import Field

from src.dtos.requests.base import BaseRequest


class QuestionCreateRequest(BaseRequest):
    script: str = Field(..., description="video subtitle", examples=["this is video test script"])
    count: int = Field(1, description="number of question")
