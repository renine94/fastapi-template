from fastapi import HTTPException
from starlette.responses import JSONResponse


class CustomException(HTTPException):
    status_code: int
    detail: str

    def __init__(self, detail=None):
        if not detail:
            detail = self.detail
        super().__init__(status_code=self.status_code, detail=detail)


async def custom_exception_handler(request, exc: CustomException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_type": exc.__class__.__name__,
            "status_code": exc.status_code,
            "detail": exc.detail,
        },
    )


# 400
class ValueException(CustomException):
    status_code = 400
    detail = "invalid value"


class NotFoundException(CustomException):
    status_code = 404
    detail = "Not found."


# 500
class ServerException(CustomException):
    status_code = 500
    detail = "Something is wrong, please try again."
