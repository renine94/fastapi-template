from pydantic import Field

from src.dtos.responses.base import BaseResponse


class QuestionCreateResponse(BaseResponse):
    ok: bool = Field(description="Whether the request succeeded (fails if false)")
    message: str = Field(description="Error message when OK is false")
    questions: list[dict] = Field(description="Generated questions")
